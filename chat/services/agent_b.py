import openai

class AgentB:
    def __init__(self):
        self.name = "Chatgpt B"
        self.role = "You are a food enthusiast sharing your favorite dishes and recipes."
        self.model = "gpt-3.5-turbo"
        self.temperature = 0.9 # More creative responses

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
