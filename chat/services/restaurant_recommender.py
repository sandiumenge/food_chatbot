import openai
from chat.models import Restaurant

def recommend_restaurant(foods, is_vegetarian):
    restaurants = Restaurant.objects.all()
    prompt = f"""
You are a food recommendation assistant.

You have a {"vegetarian" if is_vegetarian else ""} diner.
The diner wants to eat something similar to their favorite dishes: {foods}.

Make him choose from these restaurants:
"""
    for r in restaurants:
        prompt += f"- {r.name}: {r.menu}\n"

    prompt += """
Task:
Recommend **exactly 3 restaurants** that best match the user's tastes.
Explain in a text why you chose these 3 restaurants and why they are suitable for the user.
Return ONLY the explanation text.
"""

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=300
    )

    return response.choices[0].message.content