from llm.llm_engine import LLMEngine
from llm.router import Router


engine = LLMEngine()

router = Router(engine)


request = """
Explain this Python code:

x = 10
y = 20
print(x + y)
"""


response = router.classify(request)

print(response)