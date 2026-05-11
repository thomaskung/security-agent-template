import pytest
from unittest.mock import MagicMock
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.outputs import ChatResult, ChatGeneration
from langchain_core.messages import AIMessage

class MockChatModel(BaseChatModel):
    def _generate(self, messages, stop=None, run_manager=None, **kwargs):
        return ChatResult(generations=[ChatGeneration(message=AIMessage(content="mock response"))])

    @property
    def _llm_type(self) -> str:
        return "mock-chat-model"

@pytest.fixture
def mock_llm():
    """Mock LLM for testing agent instantiation."""
    mock = MockChatModel()
    return mock

@pytest.fixture
def mock_fireworks_env(monkeypatch):
    """Mocks environment variables for tests."""
    monkeypatch.setenv("FIREWORKS_API_KEY", "test_key")
    monkeypatch.setenv("TAVILY_API_KEY", "test_key")
