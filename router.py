from llm.prompt_builder import PromptBuilder


class Router:


    def __init__(self, llm_engine):

        self.llm_engine = llm_engine

        self.prompt_builder = PromptBuilder()



    def classify(self, text):


        prompt = self.prompt_builder.few_shot_classification(
            text
        )


        result = self.llm_engine.generate(
            prompt
        )


        category = result.lower().strip().split()[0]


        return category