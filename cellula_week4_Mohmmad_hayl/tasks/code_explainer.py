from llm.prompt_builder import PromptBuilder


class CodeExplainer:

    def __init__(self, llm_engine):

        self.llm_engine = llm_engine
        self.prompt_builder = PromptBuilder()


    def explain(self, user_request):

        prompt = self.prompt_builder.code_explanation_prompt(
            user_request
        )

        response = self.llm_engine.generate(
            prompt
        )

        return response