from llm.llm_engine import LLMEngine
from llm.router import Router



engine = LLMEngine()


router = Router(
    engine
)



print("\nProgramming Classifier")
print("Type exit to stop\n")



while True:


    user_input = input(
        "Request: "
    )


    if user_input.lower() == "exit":
        break



    result = router.classify(
        user_input
    )


    print(
        "Category:",
        result
    )

    print()