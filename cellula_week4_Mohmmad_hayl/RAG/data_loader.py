from datasets import load_dataset


def load_humaneval_documents():
    dataset = load_dataset("openai/openai_humaneval", split="test")

    documents = []
    for item in dataset:
        documents.append({
            "id": item["task_id"],
            "question": item["prompt"],
            "answer": item["canonical_solution"],
            "metadata": {
                "entry_point": item["entry_point"],
                "test": item["test"],
                "source": "humaneval",
            },
        })

    return documents
if __name__ == "__main__":
    docs = load_humaneval_documents()
    print(len(docs))
    print(docs[0]["id"])
    print(docs[0]["question"][:200])