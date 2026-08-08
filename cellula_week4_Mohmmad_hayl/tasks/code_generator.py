import io
import contextlib
from openai import OpenAI

from config import API_KEY
from RAG.retriever import retrieve
from RAG.vector_store import build_vector_store, add_document

client = OpenAI(api_key=API_KEY)


def check_relevance(user_query, retrieved_answer):
    prompt = f"""User question:
{user_query}

Retrieved answer:
{retrieved_answer}

Is this retrieved answer relevant and correct for the user's question?
Reply with only one word: YES or NO."""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    verdict = response.choices[0].message.content.strip().upper()
    return verdict.startswith("YES")


def run_code(code_str):
    output_buffer = io.StringIO()
    try:
        with contextlib.redirect_stdout(output_buffer):
            exec(code_str, {})
        return output_buffer.getvalue()
    except Exception as e:
        return f"Error: {e}"


def run_generation(user_query):
    results = retrieve(user_query, top_k=1)
    retrieved = results[0]

    is_relevant = check_relevance(user_query, retrieved["answer"])

    if is_relevant:
        output = run_code(retrieved["answer"])
        return {
            "status": "done",
            "source": "rag",
            "code": retrieved["answer"],
            "output": output,
        }
    else:
        return {
            "status": "needs_input",
            "query": user_query,
        }


def save_and_run(user_query, user_code):
    collection = build_vector_store()
    new_id = f"user_{abs(hash(user_query))}"
    add_document(collection, new_id, user_query, user_code)

    output = run_code(user_code)
    return {
        "status": "done",
        "source": "user",
        "code": user_code,
        "output": output,
    }


class CodeGenerator:

    def generate(self, text):
        return run_generation(text)

    def save_and_run(self, text, code):
        return save_and_run(text, code)


if __name__ == "__main__":
    query = input("Enter your coding question: ")
    result = run_generation(query)

    if result["status"] == "needs_input":
        print(f"No suitable answer found.\nYour question: {result['query']}")
        print("Enter the correct answer (Python code), and type END on its own line when done:")
        lines = []
        while True:
            line = input()
            if line.strip() == "END":
                break
            lines.append(line)
        result = save_and_run(query, "\n".join(lines))

    print(result["source"])
    print(result["code"])
    print("Output:", result["output"])