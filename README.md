# Security Agent Template

A non-deterministic, hierarchical security agent built with **LangChain**, **LangGraph**, and the **DeepAgents** harness.

## Features
- **Non-Deterministic Orchestration**: Uses a senior Security Orchestrator to dynamically delegate tasks.
- **Hierarchical Sub-Agents**:
  - **Research Agent**: Deep search via Tavily.
  - **Reading Agent**: Document parsing via Microsoft MarkItDown.
  - **Learning Agent**: Long-term memory management via ChromaDB.
- **Human-in-the-Loop**: Conversational approval for memory updates.
- **RAG Integration**: Automated and explicit retrieval from ChromaDB.
- **Modern UI**: Integrated with `deep-agents-ui`.

## Prerequisites
- **Python 3.11+** (3.13 recommended)
- **Node.js 18+**
- **Fireworks AI API Key** (for Kimi 2.6)
- **Tavily API Key**

## Setup

### 1. Backend
```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install -U "langgraph-cli[inmem]"
```

### 2. Configuration
Copy `.env.example` to `.env` and fill in your API keys:
```env
FIREWORKS_API_KEY="your_key"
TAVILY_API_KEY="your_key"
```

### 3. UI
```bash
cd ui
npm install --legacy-peer-deps
```

## Running the Project

1. **Start the LangGraph Server**:
```bash
source .venv/bin/activate
langgraph dev --port 2024
```

2. **Start the UI**:
```bash
cd ui
npm run dev
```

Visit `http://localhost:3000` to interact with the agent.

## Project Structure
- `src/agent/`: Core agent logic and graph definition.
- `src/agent/subagents/`: Specialized sub-agents.
- `src/agent/tools/`: Shared security tools.
- `ui/`: React frontend (deep-agents-ui).
- `tests/`: Unit tests for agent structure.
