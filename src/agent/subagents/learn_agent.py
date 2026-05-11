from deepagents import create_deep_agent
from src.agent.llm import get_llm
from src.agent.prompts import LEARNER_INSTRUCTIONS
from src.agent.tools.chromadb_memory import save_to_memory, query_memory
from src.agent.tools.think_tool import think_tool

def get_learn_agent():
    """Creates the Security Learning Sub-Agent."""
    return create_deep_agent(
        model=get_llm(),
        tools=[save_to_memory, query_memory, think_tool],
        system_prompt=LEARNER_INSTRUCTIONS
    )
