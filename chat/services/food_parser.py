import openai
import random
import json

def parse_foods(raw_response):
    system_role = (
        "You are a helpful assistant who extracts exactly 3 foods from user text. "
        "Return a JSON object like this: "
        '{"foods": ["food1", "food2", "food3"], "is_vegetarian": true_or_false}. '
        "Determine if all foods are vegetarian."
    )
    client = openai.OpenAI()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_role},
            {"role": "user", "content": raw_response}
        ],
        temperature=0
    )
    
    text_output = response.choices[0].message.content.strip()

    try:
        data = json.loads(text_output)
        foods = data.get("foods", [])
        is_vegetarian = data.get("is_vegetarian", False)
    except json.JSONDecodeError:
        foods = []
        is_vegetarian = False

    return foods, is_vegetarian