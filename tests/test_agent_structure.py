import pytest
from unittest.mock import MagicMock
from src.agent.graph import create_security_agent

def test_agent_instantiation(mock_llm, mock_fireworks_env, monkeypatch):
    """Verifies that the main agent and sub-agents can be instantiated correctly."""
    
    # Patch resolve_model in deepagents to return our mock directly
    # This prevents it from trying to parse our mock as a string spec
    monkeypatch.setattr("deepagents.graph.resolve_model", lambda x: mock_llm)
    
    agent = create_security_agent()
    
    assert agent is not None
    # create_deep_agent returns a CompiledGraph (LangGraph)
    assert hasattr(agent, "get_graph")
