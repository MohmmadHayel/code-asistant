from RAG.vector_store import build_vector_store

def retrieve(query, top_k=1):
    collection = build_vector_store()

    results = collection.query(
        query_texts=[query],
        n_results=top_k,
    )

    retrieved = []
    for i in range(len(results["ids"][0])):
        retrieved.append({
            "id": results["ids"][0][i],
            "question": results["documents"][0][i],
            "answer": results["metadatas"][0][i]["answer"],
            "entry_point": results["metadatas"][0][i]["entry_point"],
            "test": results["metadatas"][0][i]["test"],
            "distance": results["distances"][0][i],
        })

    return retrieved


if __name__ == "__main__":
    query = "function that checks if two numbers are close to each other"
    result = retrieve(query, top_k=1)
    print(result[0]["id"])
    print(result[0]["distance"])
    print(result[0]["answer"])