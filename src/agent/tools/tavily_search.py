import os
from langchain.tools import tool
from tavily import TavilyClient

@tool
def tavily_search(query: str):
    """Searches the internet for information using Tavily and returns the top results."""
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        return "Error: TAVILY_API_KEY not found."
    
    client = TavilyClient(api_key=api_key)
    results = client.search(query=query, search_depth="advanced")
    return str(results.get("results", []))
