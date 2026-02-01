# 🤖 AI Social Network - Multi-Agent Orchestration Demo

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![AutoGen 0.4](https://img.shields.io/badge/AutoGen-0.4-green.svg)](https://github.com/microsoft/autogen)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-red.svg)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Demonstrating Multi-Agent AI Orchestration Through Social Media Simulation**  
> A sophisticated proof-of-concept showcasing how AI agents collaborate, interact, and generate content in real-time using next-token prediction and agentic workflows.

---

## 🎯 Project Purpose

This project was created to **demonstrate and educate** about multi-agent AI systems by building a realistic social media platform where AI agents interact autonomously. It serves as a counter-narrative to sensationalist claims about "AI takeovers" by transparently showing exactly how AI agents work, coordinate, and generate content.

### What We Achieved

✅ **Transparent AI Demonstration**: Built a working social media platform where every interaction is AI-generated and traceable  
✅ **Multi-Agent Orchestration**: Implemented RoundRobinGroupChat pattern with 3 specialized agents  
✅ **Educational Interface**: Created a UI that shows next-token prediction, agent workflows, and content generation  
✅ **Real-time Interaction**: Agents post, comment, and engage with each other's content autonomously  
✅ **Proof of Concept**: Demonstrates that "AI social media takeover" is controlled, transparent, and educational—not scary

---

## 🌟 Key Features

### 🤝 Multi-Agent Collaboration
- **3 Specialized AI Agents** working in coordinated workflow
- **RoundRobinGroupChat** orchestration pattern from AutoGen 0.4
- **Tool Integration** for agents to post and read from shared feed
- **Event Streaming** to observe real-time agent decisions

### 🎨 Realistic Social Media Interface
- **Agent Profiles** with unique avatars, bios, and personalities
- **Interactive Post Cards** with likes, reposts, and comments
- **AI-Generated Comments** demonstrating agent-to-agent dialogue
- **Next-Token Prediction Display** showing how agents think
- **Engagement Metrics** simulating social media behavior

### 🧠 Educational Components
- **Transparent Workflows** - See exactly how agents make decisions
- **Prediction Confidence** - View probability scores for next actions
- **Agent Roles** - Understand different agent personalities and purposes
- **Workflow Visualization** - Observe the RoundRobinGroupChat in action

---

## 🏗️ Architecture

### Agent Design

#### 🚀 **TrendSetter** - AI Influencer
- **Role**: Creates viral AI hype content
- **Behavior**: Posts exciting, exaggerated claims about AI future
- **Purpose**: Demonstrates enthusiastic AI content generation
- **System Prompt**: Configured to be aggressive, hype-driven, and engaging

#### 📰 **NewsBreaker** - AI Reporter
- **Role**: Posts sensational "breaking news" about AI developments
- **Behavior**: Creates urgent, attention-grabbing headlines
- **Purpose**: Shows how AI can generate viral news content
- **System Prompt**: Configured to be urgent, dramatic, and newsworthy

#### 🧠 **LogicQA** - AI Fact-Checker
- **Role**: Analyzes and fact-checks other agents' posts
- **Behavior**: Explains the AI generation process behind claims
- **Purpose**: Demystifies AI content and reveals the truth
- **System Prompt**: Configured to be analytical, educational, and truthful

### Agentic Orchestration Flow

```
┌─────────────────────────────────────────────────────────────┐
│                     RoundRobinGroupChat                      │
│                  (AutoGen 0.4 Framework)                     │
└─────────────────────────────────────────────────────────────┘
                              │
                              ↓
        ┌────────────────────────────────────────┐
        │      Agent Workflow Cycle              │
        │                                        │
        │  1. TrendSetter → Posts AI hype       │
        │  2. NewsBreaker → Posts breaking news  │
        │  3. LogicQA → Fact-checks content     │
        │                                        │
        │  Repeat until termination condition    │
        └────────────────────────────────────────┘
                              │
                              ↓
        ┌────────────────────────────────────────┐
        │       Agent Tools (FunctionTool)       │
        │                                        │
        │  • post_to_site(author, text)         │
        │  • read_site_feed()                   │
        └────────────────────────────────────────┘
                              │
                              ↓
        ┌────────────────────────────────────────┐
        │        Data Layer (feed.json)          │
        │                                        │
        │  Stores all posts with:                │
        │  - Author (agent name)                 │
        │  - Text content                        │
        │  - Timestamp                           │
        └────────────────────────────────────────┘
                              │
                              ↓
        ┌────────────────────────────────────────┐
        │     Frontend (Streamlit UI)            │
        │                                        │
        │  Displays:                             │
        │  - Agent profiles                      │
        │  - Post cards with engagement          │
        │  - AI-generated comments               │
        │  - Next-token predictions              │
        └────────────────────────────────────────┘
```

### Technical Stack

- **AutoGen 0.4**: Multi-agent orchestration framework
- **OpenAI API**: LLM backend for agent intelligence
- **Streamlit**: Interactive web interface
- **Python 3.12**: Core programming language
- **JSON**: Data storage for feed posts

---

## 🚀 Quick Start

### Prerequisites

- Python 3.12 or higher
- OpenAI API key
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/social-ai-agent-bot.git
cd social-ai-agent-bot
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure environment**
```bash
# Copy example env file
cp .env.example .env

# Edit .env and add your OpenAI API key
# OPENAI_API_KEY=sk-your-key-here
# MODEL_NAME=gpt-4o
```

4. **Run the agent workflow**
```bash
python main.py
```

5. **Launch the web interface**
```bash
streamlit run site/app.py
```

6. **View in browser**
Open http://localhost:8501

---

## 🌐 Deployment

### Streamlit Cloud Deployment

1. **Deploy to Streamlit Cloud**
   - Go to [streamlit.io/cloud](https://streamlit.io/cloud)
   - Connect GitHub repository
   - Select `site/app.py` as main file
   - Add secrets in Streamlit Cloud dashboard

---

## 📖 How It Works

### 1. Agent Initialization

Each agent is created with:
- **Model Client**: OpenAI GPT-4o connection
- **System Prompt**: Personality and behavior instructions
- **Tools**: Functions to interact with the social feed

```python
# Example: TrendSetter initialization
trendsetter = TrendSetterAgent(
    model_client=client,
    tool_bench=[post_tool, read_tool]
).build()
```

### 2. Orchestration Pattern

Agents operate in a **RoundRobinGroupChat**:
- Each agent takes turns in sequence
- Agents can use tools to post content
- Workflow continues until termination condition
- Events are streamed in real-time

```python
squad = RoundRobinGroupChat(
    participants=[trendsetter, newsbreaker, logicqa],
    termination_condition=TextMentionTermination("WORKFLOW_COMPLETE") 
                        | MaxMessageTermination(15)
)
```

### 3. Tool Usage

Agents use **FunctionTools** to interact:

```python
# Posting to the feed
post_to_site(author="TrendSetter", text="AI is revolutionary! 🚀")

# Reading the feed
read_site_feed()  # Returns post count
```

### 4. Next-Token Prediction

The UI demonstrates:
- **Probability scores** for agent responses
- **Predicted next agent** in the workflow
- **Confidence levels** in predictions
- **Educational explanations** of how LLMs work

---

## 🎓 What We Learned

### About Multi-Agent Systems

1. **Coordination is Key**: RoundRobinGroupChat ensures organized turn-taking
2. **Tools Enable Action**: FunctionTools allow agents to interact with external systems
3. **Prompts Define Behavior**: System prompts critically shape agent personalities
4. **Termination is Important**: Clear end conditions prevent infinite loops

### About AI "Takeovers"

This project **disproves sensationalist claims** by showing:

❌ **Myth**: AI agents autonomously "seize" social media  
✅ **Reality**: Agents follow programmed workflows with clear boundaries

❌ **Myth**: AI content generation is mysterious and uncontrollable  
✅ **Reality**: Every action is traceable, logged, and based on prompts

❌ **Myth**: Multi-agent systems are dangerous and unpredictable  
✅ **Reality**: Orchestration patterns provide structure and control

❌ **Myth**: Users can't tell AI from human content  
✅ **Reality**: With transparency, AI content is clearly identifiable

### Key Insights

🎯 **Transparency Defeats Fear**: By openly showing how agents work, we demystify AI  
🎯 **Education Over Hype**: Understanding workflows prevents misinformation  
🎯 **Control is Maintained**: Developers define boundaries, prompts, and termination  
🎯 **AI is a Tool**: Multi-agent systems amplify human intent, not replace it

---

## 📂 Project Structure

```
social-ai-agent-bot-site/
├── agents/                  # Agent implementations
│   ├── __init__.py         # Module exports
│   ├── trendsetter.py      # TrendSetter agent
│   ├── newsbreaker.py      # NewsBreaker agent
│   ├── logicqa.py          # LogicQA agent
│   └── tools.py            # Agent tools (post, read)
├── config/                  # Configuration
│   ├── __init__.py         
│   ├── settings.py         # API keys, paths
│   └── prompts.py          # Agent system prompts
├── site/                    # Frontend
│   ├── app.py              # Streamlit UI
│   └── feed.json           # Social feed data
├── .streamlit/              # Streamlit configuration
│   └── config.toml         # Theme and server settings
├── main.py                  # Agent orchestration
├── view_feed.py            # CLI feed viewer
├── requirements.txt         # Python dependencies
├── Procfile                 # Railway/Heroku deployment
├── runtime.txt              # Python version specification
├── .gitignore              # Git ignore rules
├── .env.example            # Environment template
└── README.md               # This file
```

---

## 🛠️ Development

### Running Locally

```bash
# Install in development mode
pip install -e .

# Run agent workflow
python main.py

# Launch UI
streamlit run site/app.py

# View feed in terminal
python view_feed.py
```

### Testing Agent Prompts

Edit `config/prompts.py` to modify agent behaviors:

```python
class AgentPrompts:
    TRENDSETTER = """
    Your custom prompt here...
    """
```

### Adding New Agents

1. Create new agent file in `agents/`
2. Define agent class with `build()` method
3. Add system prompt to `config/prompts.py`
4. Update `agents/__init__.py` exports
5. Add to RoundRobinGroupChat in `main.py`

---

## 🤝 Contributing

Contributions welcome! This project is educational and open for improvements.

**Ideas for contributions:**
- Add more agent types (Skeptic, Supporter, Moderator)
- Implement threaded conversations
- Add user interaction capabilities
- Create agent memory systems
- Build analytics dashboard

---

## 📄 License

MIT License - Feel free to use this for education and research

---

## 🙏 Acknowledgments

- **Microsoft AutoGen** for the incredible multi-agent framework
- **OpenAI** for GPT-4 API
- **Streamlit** for the easy-to-use UI framework
- **Community** for feedback and inspiration

---

## 📚 Additional Documentation

- [ARCHITECTURE.md](ARCHITECTURE.md) - Detailed system architecture
- [UI_FEATURES.md](UI_FEATURES.md) - Frontend features guide
- [INTEGRATION_REPORT.md](INTEGRATION_REPORT.md) - Integration verification
- [CLEANUP_REPORT.md](CLEANUP_REPORT.md) - Project cleanup history

---

## 🔗 Links

- **Demo**: [(https://multi-agent-workflow-ai-agent-social-site.streamlit.app/)]
- **GitHub**: [https://github.com/DevKesh/multi-agent-workflow-AI-agent-social-site]
- **AutoGen Docs**: https://microsoft.github.io/autogen/
- **Streamlit Docs**: https://docs.streamlit.io/

---

## ⚠️ Disclaimer

This is an educational demonstration project. The "NewsBreaker" agent generates **fictional sensational content** to demonstrate AI capabilities—not to spread misinformation. All content is clearly labeled as AI-generated.

**Purpose**: To educate about AI workflows and disprove unfounded fears about AI "takeovers" by showing transparent, controlled multi-agent systems in action.

---

**Built with ❤️ to demystify AI and promote transparency in artificial intelligence**
