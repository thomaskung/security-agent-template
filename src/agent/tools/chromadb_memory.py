import chromadb
from langchain.tools import tool

@tool
def save_to_memory(content: str, metadata: dict = None):
    """Saves a security report or information to the long-term memory (ChromaDB)."""
    try:
        client = chromadb.PersistentClient(path="./chroma_db")
        collection = client.get_or_create_collection(name="security_knowledge")
        collection.add(
            documents=[content],
            metadatas=[metadata or {}],
            ids=[f"id_{hash(content)}"]
        )
        return "Successfully saved to memory."
    except Exception as e:
        return f"Error saving to memory: {e}"

@tool
def query_memory(query: str, n_results: int = 3):
    """Queries the long-term memory (ChromaDB) for relevant security information."""
    try:
        client = chromadb.PersistentClient(path="./chroma_db")
        collection = client.get_or_create_collection(name="security_knowledge")
        results = collection.query(query_texts=[query], n_results=n_results)
        return str(results.get("documents", []))
    except Exception as e:
        return f"Error querying memory: {e}"
