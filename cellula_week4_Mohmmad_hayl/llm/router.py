from llm.prompt_builder import PromptBuilder
from tasks.code_explainer import CodeExplainer


class Router:

    def __init__(self, llm_engine):

        self.llm_engine = llm_engine

        self.prompt_builder = PromptBuilder()

        self.explainer = CodeExplainer(
            llm_engine
        )


    def classify(self, text):

        prompt = self.prompt_builder.few_shot_classification(
            text
        )

        result = self.llm_engine.generate(
            prompt
        )

        category = result.lower().strip().split()[0]


        if category == "explain":

            return self.explainer.explain(
                text
            )


        elif category == "generate":

            return "Generate task not implemented yet."


        else:

            return "Invalid request."