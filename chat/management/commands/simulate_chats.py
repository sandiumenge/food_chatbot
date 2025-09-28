from django.core.management.base import BaseCommand
import openai
import os
from chat.services import AgentA, AgentB, parse_foods
from chat.models import UserProfile
import time

openai.api_key = os.environ.get("OPENAI_API_KEY")
if not openai.api_key:
    raise RuntimeError("OPENAI_API_KEY not set in environment")

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, default=100, help="Number of chats to simulate")

    def handle(self, *args, **options):
        count = options['count']
        agent_a = AgentA()
        agent_b = AgentB()

        max_consecutive_errors = 3
        consecutive_errors = 0
        i = 0

        while i < count:
            task = "Ask the interviewed what are their 3 favourite foods?"
            try:
                question = agent_a.ask_question(task)
                response = agent_b.respond_to_question(question)
                foods, is_vegetarian = parse_foods(response)

                UserProfile.objects.create(
                    username=f"{agent_b.name}_{i+1}",
                    foods=foods,
                    raw_responses=response,
                    is_vegetarian=is_vegetarian
                )
                
                i += 1                      # Only increment when successful
                consecutive_errors = 0      # Reset on success

            except Exception as e:
                consecutive_errors += 1
                self.stdout.write(
                    self.style.ERROR(
                        f"Error during chat simulation {i+1} (consecutive {consecutive_errors}): {e}"
                    )
                )

                if consecutive_errors >= max_consecutive_errors:
                    self.stdout.write(
                        self.style.ERROR(
                            f"Stopping execution after {consecutive_errors} consecutive errors at simulation {i+1}"
                        )
                    )
                    break
            time.sleep(0.3)  # To avoid hitting rate limits