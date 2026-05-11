from langchain.tools import tool
try:
    from markitdown import MarkItDown
except ImportError:
    MarkItDown = None

@tool
def markitdown_reader(file_path: str):
    """Converts a document (PDF, Word, etc.) to Markdown and returns the text content."""
    if not MarkItDown:
        return "Error: markitdown library not installed."
    
    try:
        md = MarkItDown()
        result = md.convert(file_path)
        return result.text_content
    except Exception as e:
        return f"Error reading document: {e}"
