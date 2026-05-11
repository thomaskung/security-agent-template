from deepagents import create_deep_agent
from src.agent.llm import get_llm
from src.agent.prompts import RESEARCHER_INSTRUCTIONS
from src.agent.tools.tavily_search import tavily_search
from src.agent.tools.think_tool import think_tool

def get_research_agent():
    """Creates the Security Research Sub-Agent."""
    return create_deep_agent(
        model=get_llm(),
        tools=[tavily_search, think_tool],
        system_prompt=RESEARCHER_INSTRUCTIONS
    )
