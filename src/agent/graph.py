from langgraph.checkpoint.memory import MemorySaver
from deepagents import create_deep_agent
from src.agent.llm import get_llm
from src.agent.prompts import MAIN_AGENT_INSTRUCTIONS
from src.agent.tools.think_tool import think_tool
from src.agent.tools.chromadb_memory import query_memory
from src.agent.subagents.research_agent import get_research_agent
from src.agent.subagents.read_agent import get_read_agent
from src.agent.subagents.learn_agent import get_learn_agent

def create_security_agent():
    """Initializes the main non-deterministic Security Agent with sub-agents and tools."""
    
    # Initialize checkpointer
    checkpointer = MemorySaver()

    # Instantiate sub-agents
    research_sub_agent = get_research_agent()
    read_sub_agent = get_read_agent()
    learn_sub_agent = get_learn_agent()
    
    # Create the main agent
    agent = create_deep_agent(
        model=get_llm(),
        tools=[think_tool, query_memory],
        system_prompt=MAIN_AGENT_INSTRUCTIONS,
        subagents=[
            {
                "name": "research_agent",
                "description": "Searches the internet for security information and creates Markdown reports.",
                "runnable": research_sub_agent
            },
            {
                "name": "read_agent",
                "description": "Processes documents and summarizes key takeaways.",
                "runnable": read_sub_agent
            },
            {
                "name": "learn_agent",
                "description": "Evaluates and stores information in long-term memory (ChromaDB).",
                "runnable": learn_sub_agent
            }
        ],
        checkpointer=checkpointer
    )
    
    return agent
