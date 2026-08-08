class PromptBuilder:

    def __init__(self):

        self.labels = [
            "generate",
            "explain",
            "invalid"
        ]

        self.examples = [

            {
                "text": "Write a Python function that reverses a string.",
                "label": "generate"
            },

            {
                "text": "Create a Java class for a bank account.",
                "label": "generate"
            },

            {
                "text": "Explain what this Python code does.",
                "label": "explain"
            },

            {
                "text": "Why does this code throw an error?",
                "label": "explain"
            },

            {
                "text": "What is the capital of France?",
                "label": "invalid"
            }
        ]


    def few_shot_classification(self, text):

        prompt = (
            "You are a programming request classifier.\n"
            f"Classify the request into one category: "
            f"{', '.join(self.labels)}.\n\n"

            "Rules:\n"
            "- Code creation requests -> generate\n"
            "- Code explanation requests -> explain\n"
            "- Non programming requests -> invalid\n"

            "Return only one word.\n\n"

            "Examples:\n"
        )


        for example in self.examples:

            prompt += (
                f"User: {example['text']}\n"
                f"Category: {example['label']}\n\n"
            )


        prompt += (
            f"User: {text}\n"
            "Category:"
        )

        return prompt


    def code_explanation_prompt(self, text):

        prompt = f"""
You are a programming expert.

Explain the following programming request clearly.

Include:
- What the code does
- Why it works
- Any errors or improvements if needed

User request:
{text}

Explanation:
"""

        return prompt