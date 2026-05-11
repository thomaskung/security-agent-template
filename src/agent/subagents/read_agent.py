from deepagents import create_deep_agent
from src.agent.llm import get_llm
from src.agent.prompts import READER_INSTRUCTIONS
from src.agent.tools.markitdown_reader import markitdown_reader
from src.agent.tools.think_tool import think_tool

def get_read_agent():
    """Creates the Security Document Reading Sub-Agent."""
    return create_deep_agent(
        model=get_llm(),
        tools=[markitdown_reader, think_tool],
        system_prompt=READER_INSTRUCTIONS
    )
