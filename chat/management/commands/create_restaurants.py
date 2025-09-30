import json
import openai
from django.core.management.base import BaseCommand
from chat.models import Restaurant
import random
import time
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")
if not openai.api_key:
    raise RuntimeError("OPENAI_API_KEY not set in environment")

class Command(BaseCommand):
    help = "Generate restaurants with name and 5-dish menu using ChatGPT"

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, default=20, help='Number of restaurants to generate')

    def print_progress(self, current, total):
        percent = int((current / total) * 100)
        bar = "█" * (percent // 2) + "-" * (50 - percent // 2)
        self.stdout.write(f"\r|{bar}| {percent}%", ending="")
        self.stdout.flush()

    def handle(self, *args, **options):
        count = options['count']

        styles = [
            "Italian Trattoria", "Sushi Bar", "BBQ Smokehouse",
            "French Bistro", "Vegan Café", "Mexican Taqueria",
            "Thai Kitchen", "Dessert Parlor", "Burger Joint", "Steakhouse",
            "Dim Sum House", "Mediterranean Grill", "Korean BBQ", "Fusion Restaurant",
            "Seafood Shack", "Tapas Bar", "Indian Curry House", "Middle Eastern Mezze",
            "Health Bowl Spot", "Pizza Place"
        ]

        max_consecutive_errors = 3
        consecutive_errors = 0
        i = 0

        while i < count:
            style = random.choice(styles)
            prompt = f"""
Given the restaurant style "{style}", generate a restaurant name and a menu of exactly 5 dishes.
Return ONLY valid JSON like: {{"name":"...","menu":["dish1","dish2","dish3","dish4","dish5"]}}
"""
            try:
                response = openai.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role":"user","content":prompt}],
                    temperature=0.9
                )
                data = json.loads(response.choices[0].message.content)

                Restaurant.objects.create(
                    name=data['name'],
                    menu=data['menu']
                )

                i += 1                      # Only increment when successful
                consecutive_errors = 0      # Reset on success
                self.print_progress(i, count)

            except Exception as e:
                consecutive_errors += 1
                self.stdout.write(
                    self.style.ERROR(
                        f"\nError generating restaurant {i+1} (consecutive {consecutive_errors}): {e}"
                    )
                )

                if consecutive_errors >= max_consecutive_errors:
                    self.stdout.write(
                        self.style.ERROR(
                            f"\nStopping execution after {consecutive_errors} consecutive errors at restaurant {i+1}"
                        )
                    )
                    break

            time.sleep(0.3)  # To avoid hitting rate limits


        
