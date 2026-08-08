from llm.llm_engine import LLMEngine
from llm.router import Router


engine = LLMEngine()

router = Router(engine)


request = """
generate a function that reverses a string
"""


response = router.classify(request)

print(response)