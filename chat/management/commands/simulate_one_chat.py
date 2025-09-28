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
    def handle(self, *args, **options):
        agent_a = AgentA()
        agent_b = AgentB()

        task = "Ask the interviewed what are their 3 favourite foods?"
        try:
            question = agent_a.ask_question(task)
            response = agent_b.respond_to_question(question)
            foods, is_vegetarian = parse_foods(response)

            UserProfile.objects.create(
                username=agent_b.name,
                foods=foods,
                raw_responses=response,
                is_vegetarian=is_vegetarian
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(
                    f"Error during chat simulation: {e}"
                )
            )