import openai

class AgentA:
    def __init__(self):
        self.name = "Chatgpt A"
        self.role = "You are a friendly interviewer asking about food preferences."
        self.model = "gpt-3.5-turbo"
        self.temperature = 0.7

    def ask_question(self, question):
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
        return response.choices[0].message.content.strip()