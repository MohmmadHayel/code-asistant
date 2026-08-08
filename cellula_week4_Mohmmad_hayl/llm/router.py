from llm.prompt_builder import PromptBuilder
from tasks.code_explainer import CodeExplainer
from tasks.code_generator import CodeGenerator


class Router:

    def __init__(self, llm_engine):

        self.llm_engine = llm_engine

        self.prompt_builder = PromptBuilder()

        self.explainer = CodeExplainer(
            llm_engine
        )

        self.generator = CodeGenerator()


    def classify(self, text):

        prompt = self.prompt_builder.few_shot_classification(
            text
        )

        result = self.llm_engine.generate(
            prompt
        )

        category = result.lower().strip().split()[0]


        if category == "explain":

            return {
                "task": "explain",
                "result": self.explainer.explain(text),
            }


        elif category == "generate":

            return {
                "task": "generate",
                "result": self.generator.generate(text),
            }


        else:

            return {
                "task": "invalid",
                "result": "Invalid request.",
            }