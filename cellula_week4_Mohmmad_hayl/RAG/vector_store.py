import chromadb
from chromadb.utils import embedding_functions

from RAG.data_loader import load_humaneval_documents

def build_vector_store(persist_dir="chroma_db", collection_name="humaneval_code"):
    client = chromadb.PersistentClient(path=persist_dir)

    embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )

    collection = client.get_or_create_collection(
        name=collection_name,
        embedding_function=embedding_fn,
    )

    if collection.count() > 0:
        return collection

    documents = load_humaneval_documents()

    collection.add(
        ids=[doc["id"] for doc in documents],
        documents=[doc["question"] for doc in documents],
        metadatas=[
            {
                "answer": doc["answer"],
                "entry_point": doc["metadata"]["entry_point"],
                "test": doc["metadata"]["test"],
                "source": doc["metadata"]["source"],
            }
            for doc in documents
        ],
    )

    return collection

def add_document(collection, doc_id, question, answer, entry_point="", test=""):
    collection.add(
        ids=[doc_id],
        documents=[question],
        metadatas=[{
            "answer": answer,
            "entry_point": entry_point,
            "test": test,
            "source": "user",
        }],
    )


if __name__ == "__main__":
    collection = build_vector_store()
    print(collection.count())