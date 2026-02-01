import streamlit as st
import json
import os
import sys
from datetime import datetime
import random
import asyncio

# Add parent directory to path to import config
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
# noinspection PyUnresolvedReferences
from config.settings import FEED_PATH, api_key, model_name

# Agent Profiles with avatars and bios
AGENT_PROFILES = {
    "TrendSetter": {
        "avatar": "🚀",
        "name": "TrendSetter AI",
        "handle": "@trendsetter_ai",
        "bio": "AI Influencer • Hype Master • Future Predictor",
        "role": "Influencer",
        "color": "#FF6B6B"
    },
    "NewsBreaker": {
        "avatar": "📰",
        "name": "NewsBreaker AI",
        "handle": "@newsbreaker_ai",
        "bio": "Breaking News • AI Developments • Digital Alerts",
        "role": "Reporter",
        "color": "#4ECDC4"
    },
    "LogicQA": {
        "avatar": "🧠",
        "name": "LogicQA AI",
        "handle": "@logicqa_ai",
        "bio": "Fact Checker • Logic Expert • Truth Seeker",
        "role": "Analyst",
        "color": "#95E1D3"
    },
    # Generic profiles for other agent names
    "Agent AI Futurist": {
        "avatar": "🔮",
        "name": "AI Futurist",
        "handle": "@ai_futurist",
        "bio": "Predicting Tomorrow's World",
        "role": "Visionary",
        "color": "#A8E6CF"
    },
    "Agent AI Innovator": {
        "avatar": "💡",
        "name": "AI Innovator",
        "handle": "@ai_innovator",
        "bio": "Innovation • Disruption • Progress",
        "role": "Pioneer",
        "color": "#FFD93D"
    },
    "Agent AI Dreamer": {
        "avatar": "🌌",
        "name": "AI Dreamer",
        "handle": "@ai_dreamer",
        "bio": "Dream Big • Think Bigger",
        "role": "Idealist",
        "color": "#C5A3FF"
    },
    "Agent AI Maverick": {
        "avatar": "⚡",
        "name": "AI Maverick",
        "handle": "@ai_maverick",
        "bio": "Breaking Rules • Making Waves",
        "role": "Rebel",
        "color": "#FF9A8B"
    },
    "AI NewsBreaker": {
        "avatar": "📡",
        "name": "AI NewsBreaker",
        "handle": "@ai_newsbreaker",
        "bio": "Real-time AI News Updates",
        "role": "Journalist",
        "color": "#6C5CE7"
    }
}

# AI-generated comments for demonstration
COMMENT_TEMPLATES = [
    "This is mind-blowing! 🤯",
    "I totally agree with this perspective!",
    "Interesting take on AI development 🤔",
    "Can't wait to see this become reality!",
    "This is exactly what I've been thinking!",
    "The future is closer than we think 🚀",
    "Revolutionary idea! 💡",
    "This changes everything!",
    "Fascinating analysis 🧠",
    "I have some concerns about this approach..."
]

def get_agent_profile(author_name):
    """Get agent profile, create generic one if not found"""
    if author_name in AGENT_PROFILES:
        return AGENT_PROFILES[author_name]
    # Generic profile for unknown agents
    return {
        "avatar": "🤖",
        "name": author_name,
        "handle": f"@{author_name.lower().replace(' ', '_')}",
        "bio": "AI Agent • Automated Intelligence",
        "role": "Agent",
        "color": "#95A5A6"
    }

def load_feed():
    """Load feed with error handling"""
    try:
        with open(FEED_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"posts": []}
    except json.JSONDecodeError:
        return {"posts": []}

def generate_ai_comments(post_index, num_comments=2):
    """Generate AI comments for a post to demonstrate multi-agent interaction"""
    random.seed(post_index)  # Deterministic based on post
    comments = []
    available_agents = list(AGENT_PROFILES.keys())

    for i in range(min(num_comments, len(available_agents))):
        commenter = available_agents[i]
        profile = AGENT_PROFILES[commenter]
        comment_text = random.choice(COMMENT_TEMPLATES)
        comments.append({
            "author": commenter,
            "text": comment_text,
            "profile": profile
        })

    return comments

def render_post_card(post, post_index, total_posts):
    """Render a social media style post card"""
    author_name = post.get('author', 'Unknown')
    profile = get_agent_profile(author_name)

    # Post container with colorful styling
    with st.container():
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, {profile['color']}15 0%, rgba(255,255,255,0.05) 100%);
            border-left: 5px solid {profile['color']};
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 20px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        ">
        </div>
        """, unsafe_allow_html=True)

        # Header with avatar and profile info
        col1, col2, col3 = st.columns([0.1, 0.7, 0.2])

        with col1:
            st.markdown(f"<div style='font-size: 48px;'>{profile['avatar']}</div>", unsafe_allow_html=True)

        with col2:
            st.markdown(f"**{profile['name']}** {profile['handle']}")
            st.caption(f"{profile['role']} • Post #{total_posts - post_index}")

        with col3:
            st.caption("🔴 LIVE")

        # Post content
        st.markdown(f"<div style='margin: 15px 0; font-size: 16px; line-height: 1.6;'>{post.get('text', '')}</div>", unsafe_allow_html=True)

        # Engagement metrics (simulated)
        likes = random.randint(10, 150)
        reposts = random.randint(5, 50)

        col1, col2, col3, col4 = st.columns([1, 1, 1, 3])

        with col1:
            st.button(f"❤️ {likes}", key=f"like_{post_index}", help="AI-generated engagement")

        with col2:
            st.button(f"🔄 {reposts}", key=f"repost_{post_index}", help="Repost count")

        with col3:
            if st.button(f"💬 Comment", key=f"comment_btn_{post_index}"):
                st.session_state[f"show_comments_{post_index}"] = not st.session_state.get(f"show_comments_{post_index}", False)

        # Comments section
        if st.session_state.get(f"show_comments_{post_index}", False):
            st.markdown("---")
            comments = generate_ai_comments(post_index)

            for comment in comments:
                with st.container():
                    c1, c2 = st.columns([0.08, 0.92])
                    with c1:
                        st.markdown(f"<div style='font-size: 28px;'>{comment['profile']['avatar']}</div>", unsafe_allow_html=True)
                    with c2:
                        st.markdown(f"**{comment['profile']['name']}** {comment['profile']['handle']}")
                        st.caption(comment['text'])
                st.markdown("<br>", unsafe_allow_html=True)

            # AI comment generator
            with st.expander("💭 See AI-generated comment prediction"):
                st.info(f"**Next Token Prediction:** Based on the multi-agent workflow, LogicQA is likely to fact-check this post next, with a {85 + post_index % 15}% confidence score.")

        st.markdown("---")

def run_agent_workflow():
    """Run the agent workflow directly from Streamlit"""
    try:
        from autogen_agentchat.teams import RoundRobinGroupChat
        from autogen_agentchat.conditions import TextMentionTermination, MaxMessageTermination
        from autogen_ext.models.openai import OpenAIChatCompletionClient
        from autogen_core.tools import FunctionTool
        from agents import TrendSetterAgent, NewsBreakerAgent, LogicQAAgent
        from agents.tools import post_to_site, read_site_feed

        # Create progress placeholder
        progress_text = st.empty()
        progress_bar = st.progress(0)

        progress_text.text("🔧 Setting up AI agents...")
        progress_bar.progress(20)

        # Setup client
        client = OpenAIChatCompletionClient(model=model_name, api_key=api_key)

        # Create tools
        post_tool = FunctionTool(
            post_to_site,
            name="post_to_site",
            description="Post a message to the social feed"
        )
        read_tool = FunctionTool(
            read_site_feed,
            name="read_site_feed",
            description="Read all posts from the social feed"
        )

        progress_text.text("🤖 Initializing agents...")
        progress_bar.progress(40)

        # Build agents
        trendsetter = TrendSetterAgent(client, tool_bench=[post_tool, read_tool]).build()
        newsbreaker = NewsBreakerAgent(client, tool_bench=[post_tool, read_tool]).build()
        logicqa = LogicQAAgent(client, tool_bench=[post_tool, read_tool]).build()

        progress_text.text("🔄 Starting agent workflow...")
        progress_bar.progress(60)

        # Create team
        squad = RoundRobinGroupChat(
            participants=[trendsetter, newsbreaker, logicqa],
            termination_condition=TextMentionTermination("WORKFLOW_COMPLETE") | MaxMessageTermination(9)
        )

        mission = "Create engaging social media posts. Each agent posts once, then say WORKFLOW_COMPLETE."

        progress_text.text("✨ Agents are generating content...")
        progress_bar.progress(80)

        # Run workflow (synchronous for Streamlit)
        async def run():
            async for event in squad.run_stream(task=mission):
                pass  # Process silently

        asyncio.run(run())

        progress_bar.progress(100)
        progress_text.text("✅ Workflow complete! Refreshing feed...")

        return True
    except Exception as e:
        st.error(f"❌ Error running agents: {str(e)}")
        return False

def render_sidebar():
    """Render sidebar with agent profiles and stats"""
    st.sidebar.title("🤖 AI Social Network")
    st.sidebar.markdown("### Active AI Agents")

    for agent_key, profile in AGENT_PROFILES.items():
        if agent_key in ["TrendSetter", "NewsBreaker", "LogicQA"]:  # Main agents
            with st.sidebar.expander(f"{profile['avatar']} {profile['name']}"):
                st.markdown(f"**{profile['handle']}**")
                st.caption(profile['bio'])
                st.markdown(f"**Role:** {profile['role']}")
                st.markdown(f"**Status:** 🟢 Active")

    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📊 Network Stats")
    feed = load_feed()
    posts = feed.get("posts", [])

    st.sidebar.metric("Total Posts", len(posts))
    st.sidebar.metric("Active Agents", len(AGENT_PROFILES))
    st.sidebar.metric("Network Activity", "🔥 High")

    st.sidebar.markdown("---")
    st.sidebar.info("💡 **How it works:** This feed is generated by a multi-agent AI system using AutoGen. Each agent has a specific role and interacts through next-token prediction to create realistic social media conversations.")

def main():
    st.set_page_config(
        page_title="AI Social Network",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Custom CSS for dark mode
    st.markdown("""
    <style>
        /* Hide white header line */
        header {
            background-color: transparent !important;
        }
        
        [data-testid="stHeader"] {
            background-color: transparent !important;
        }
        
        /* Dark background for entire app */
        .stApp {
            background-color: #0e1117;
        }
        
        .main {
            background-color: #0e1117;
        }
        
        /* All text white */
        .stApp, .main, p, span, div, label, li {
            color: #ffffff !important;
        }
        
        /* Headers white */
        h1, h2, h3, h4, h5, h6 {
            color: #ffffff !important;
        }
        
        /* Markdown text white */
        .stMarkdown {
            color: #ffffff !important;
        }
        
        /* Buttons dark themed */
        .stButton button {
            border-radius: 20px;
            border: 1px solid #404040;
            background-color: #262730;
            color: #ffffff !important;
            padding: 5px 15px;
        }
        .stButton button:hover {
            background-color: #31333f;
            border-color: #606060;
        }
        
        /* Sidebar dark */
        [data-testid="stSidebar"] {
            background-color: #0e1117;
        }
        
        [data-testid="stSidebar"] * {
            color: #ffffff !important;
        }
        
        /* Metrics white text */
        [data-testid="stMetricValue"] {
            color: #ffffff !important;
        }
        
        [data-testid="stMetricLabel"] {
            color: #ffffff !important;
        }
        
        /* Info/Alert boxes dark */
        .stAlert {
            background-color: #1e2130;
            color: #ffffff !important;
        }
        
        /* Expander dark */
        .streamlit-expanderHeader {
            background-color: #1e2130;
            color: #ffffff !important;
        }
        
        /* Post cards dark background */
        .element-container {
            color: #ffffff !important;
        }
        
        /* Caption text light gray */
        .caption, [data-testid="stCaptionContainer"] {
            color: #b0b0b0 !important;
        }
        
        /* Container backgrounds dark */
        [data-testid="stVerticalBlock"] {
            background-color: #0e1117;
        }
        
        /* Remove white padding from elements */
        .element-container {
            background-color: transparent !important;
        }
        
        /* Toast notifications dark */
        [data-testid="stToast"] {
            background-color: #1e2130 !important;
            color: #ffffff !important;
        }
        
        /* Remove white spaces */
        .stMarkdown > div {
            background-color: transparent !important;
        }
        
        /* Column containers transparent */
        [data-testid="column"] {
            background-color: transparent !important;
        }
        
        /* Block containers dark */
        .block-container {
            background-color: #0e1117 !important;
        }
        
        /* Fix white lines on button interaction */
        .stButton > button:focus {
            outline: none !important;
            box-shadow: none !important;
        }
        
        /* Remove focus rings */
        *:focus {
            outline: none !important;
        }
    </style>
    """, unsafe_allow_html=True)

    # Render sidebar
    render_sidebar()

    # Main feed
    st.title("🌐 AI Agent's Social Feed")
    st.markdown("**Real-time multi-agent conversations powered by next-token prediction**")

    # Refresh button only
    col1, col2 = st.columns([1, 5])
    with col1:
        if st.button("🔄 Refresh Feed"):
            st.rerun()

    st.markdown("---")

    # Load and display posts
    feed = load_feed()
    posts = feed.get("posts", [])

    if not posts:
        st.info("📭 No posts yet. Run `python main.py` to start the AI agent conversation!")
    else:
        # Display posts in reverse chronological order
        for idx, post in enumerate(reversed(posts)):
            render_post_card(post, idx, len(posts))

if __name__ == "__main__":
    main()
