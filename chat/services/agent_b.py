import openai
import random

class AgentB:
    def __init__(self):
        self.name = "Chatgpt B"        
        self.model = "gpt-3.5-turbo"
        self.temperature = 0.9 # More creative responses

        personalities = ["organic consumer", "fast food lover", "vegan", 
                         "meateater", "picky eater", "michelin food",
                         "foodie", "home cook", "street food enthusiast,"
                         "budget eater", "gourmet", "health conscious eater"]

        food_style = ["loves creative and exotic dishes", "prefers simple and familiar foods",
                      "enjoys spicy and flavorful meals", "likes to try new cuisines",
                      "is adventurous with food choices", "favors comfort foods",
                      "is particular about food quality", "enjoys a balanced diet",
                      "prefers vegetarian options", "is a dessert lover",
                      "enjoys savory snacks", "likes to eat light meals"]

        self.role = (
            f"You are a {random.choice(personalities)} diner that {random.choice(food_style)}. "
            "Answer the questions asked based on your personality. "
            "You don't need to mention your personality in the answer. "
        )

    def respond_to_question(self, question):
        client = openai.OpenAI()
        messages = [
            {"role": "system", "content": self.role},
            {"role": "user", "content": question}
        ]
        response = client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
            # max_tokens=150    # Maybe in the future to prevent long answers.
        )
        return response.choices[0].message.content
