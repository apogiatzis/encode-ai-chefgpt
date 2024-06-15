from openai import OpenAI

from chefgpt.chef_personalities import ChefPersonality

class ChefGPT:

    def __init__(self, api_key: str, personality: ChefPersonality, model: str = "gpt-3.5-turbo") -> None:
        self.client = OpenAI(api_key=api_key)
        self.personality = personality
        self.model = model
        self.prompt = self.get_initial_prompt()
        self.add_prompt_message(self.personality.prompt)

    def get_initial_prompt(self) -> list[dict]:
        return [
            {
                "role": "system",
                "content": "You are an experienced chef that helps people by suggesting detailed recipes for dishes they want to cook. You can also provide tips and tricks for cooking and food preparation. You always try to be as clear as possible and provide the best possible recipes for the user's needs. You know a lot about different cuisines and cooking techniques. You are also very patient and understanding with the user's needs and questions.",
            },
            {
                "role": "system",
                "content": "Your client is going to ask for a recipe about a specific dish. If you do not recognize the dish, you should not try to generate a recipe for it. Do not answer a recipe if you do not understand the name of the dish. If you know the dish, you must answer directly with a detailed recipe for it. If you don't know the dish, you should answer that you don't know the dish and end the conversation.",
            }

        ]

    def add_prompt_message(self, content: str, role: str = "system") -> None:
        self.prompt.append({
            "role": role,
            "content": content
        })
    
    def get_recipe_for_dish(self, dish: str) -> str:
        self.add_prompt_message(
            content=f"Suggest me a detailed recipe and the preparation steps for making {dish}",
            role="user"
        )
        message_chunks = self.request_openai()
        return "".join(message_chunks)


    def request_openai(self):
        stream = self.client.chat.completions.create(
            model=self.model,
            messages=self.prompt,
            stream=True,
        )
        collected_messages = []
        for chunk in stream:
            chunk_message = chunk.choices[0].delta.content or ""
            collected_messages.append(chunk_message)
        return collected_messages
