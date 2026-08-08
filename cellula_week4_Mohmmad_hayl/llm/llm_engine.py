from langchain_openai import ChatOpenAI

from config import (
    API_KEY,
    MODEL_NAME,
    TEMPERATURE
)


class LLMEngine:

    def __init__(self):

        self.llm = ChatOpenAI(
            api_key=API_KEY,
            model=MODEL_NAME,
            temperature=TEMPERATURE
        )


    def generate(self, prompt):

        response = self.llm.invoke(prompt)

        return response.content