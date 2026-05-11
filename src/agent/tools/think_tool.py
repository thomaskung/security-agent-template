from langchain.tools import tool

@tool
def think_tool(reflection: str):
    """A strategic reflection tool. Use this to pause, assess progress, and plan next steps internally."""
    return f"Reflection noted: {reflection}"
