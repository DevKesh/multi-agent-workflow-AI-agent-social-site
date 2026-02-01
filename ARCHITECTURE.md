# Project Structure Comparison

## Agent_Architecture_Executor Structure (Reference)
```
Agent_Architecture_Executor/
├── agents/
│   ├── __init__.py          # System path fix + exports
│   ├── planner.py          # PlannerAgent class
│   ├── analyst.py          # AnalystAgent class
│   ├── coder.py            # CoderAgent class
│   ├── critic.py           # CriticAgent class
│   └── executor.py         # ExecutorAgent class
├── config/
│   ├── __init__.py
│   ├── prompts.py          # AgentPrompts class with system messages
│   └── settings.py         # API keys and configuration
├── tests/                  # Generated test files
├── main.py                 # Async orchestration with RoundRobinGroupChat
└── requirements.txt
```

## social-ai-agent-bot-site Structure (Implemented)
```
social-ai-agent-bot-site/
├── agents/
│   ├── __init__.py          # System path fix + exports
│   ├── trendsetter.py      # TrendSetterAgent class
│   ├── newsbreaker.py      # NewsBreakerAgent class
│   ├── logicqa.py          # LogicQAAgent class
│   └── tools.py            # post_to_site() and read_site_feed()
├── config/
│   ├── __init__.py
│   ├── prompts.py          # AgentPrompts class with system messages
│   └── settings.py         # API keys and configuration
├── site/
│   ├── feed.json           # Social feed data storage
│   └── app.py              # Streamlit frontend
├── main.py                 # Async orchestration with RoundRobinGroupChat
├── requirements.txt
├── README.md
└── .env.example
```

## Key Architectural Similarities

### 1. Agent Structure
Both projects use the same agent class pattern:
```python
class AgentName:
    def __init__(self, model_client, tool_bench=None):
        self.model_client = model_client
        self.name = "AgentName"
        self.tool_bench = tool_bench if tool_bench else []
        self.system_message = AgentPrompts.AGENT_NAME
    
    def build(self) -> AssistantAgent:
        return AssistantAgent(
            name=self.name,
            model_client=self.model_client,
            tools=self.tool_bench,
            system_message=self.system_message
        )
```

### 2. Config Structure
- `config/prompts.py`: AgentPrompts class with structured system messages
- `config/settings.py`: API keys and environment configuration
- `config/__init__.py`: Package initialization

### 3. Main.py Orchestration Pattern
Both use:
- `async def main()` with asyncio.run()
- OpenAIChatCompletionClient initialization
- FunctionTool wrapping for custom functions
- Agent building with dependency injection (tool_bench)
- RoundRobinGroupChat for sequential agent execution
- TextMentionTermination + MaxMessageTermination
- async for event in squad.run_stream(task=mission)
- Event handling with source/content attributes

### 4. Agents Package
- `agents/__init__.py`: System path fix + clean exports
- Individual agent files as classes
- Imported as: `from agents import AgentName`

## Workflow Comparison

### Agent_Architecture_Executor Workflow
1. Planner: Active browser testing
2. Analyst: Approve automatable scenarios
3. Coder: Write test files
4. Critic: Audit the code
5. Executor: Run tests and generate reports

### social-ai-agent-bot-site Workflow
1. TrendSetter: Create AI hype posts
2. NewsBreaker: Post sensational AI news
3. LogicQA: Demystify and explain AI generation
4. Cycle repeats 3 times

## Benefits of This Architecture
1. **Separation of Concerns**: Agents, config, and tools are separated
2. **Reusability**: Agent classes can be easily modified and extended
3. **Testability**: Each component can be tested independently
4. **Scalability**: Easy to add new agents following the same pattern
5. **Maintainability**: Clear structure makes debugging easier
6. **Dependency Injection**: Tools are passed to agents, not hardcoded
