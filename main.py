import asyncio
import os
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination, MaxMessageTermination
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.tools import FunctionTool

from config.settings import api_key, model_name
# noinspection PyUnresolvedReferences
from agents import TrendSetterAgent, NewsBreakerAgent, LogicQAAgent
from agents.tools import post_to_site, read_site_feed


async def main():
    print(f"\n{'=' * 80}\n🤖 AI SOCIAL AGENT BOT: Automated Social Feed Generation\n{'=' * 80}")

    # 1. Infrastructure Setup
    os.makedirs("site", exist_ok=True)

    # 2. Setup OpenAI Client
    client = OpenAIChatCompletionClient(model=model_name, api_key=api_key)

    # 3. Create Function Tools
    print("🛠️  Equipping agents with tools...")
    post_tool = FunctionTool(
        post_to_site,
        name="post_to_site",
        description="Post a message to the social feed. Args: author (str), text (str)"
    )
    read_tool = FunctionTool(
        read_site_feed,
        name="read_site_feed",
        description="Read all posts from the social feed"
    )

    # 4. Build Agents (with tools)
    trendsetter = TrendSetterAgent(client, tool_bench=[post_tool, read_tool]).build()
    newsbreaker = NewsBreakerAgent(client, tool_bench=[post_tool, read_tool]).build()
    logicqa = LogicQAAgent(client, tool_bench=[post_tool, read_tool]).build()

    # 5. Form Squad
    squad = RoundRobinGroupChat(
        participants=[trendsetter, newsbreaker, logicqa],
        termination_condition=TextMentionTermination("WORKFLOW_COMPLETE") | MaxMessageTermination(30)
    )

    # 6. Mission Trigger
    mission = """
You are a team of AI social agents collaborating to create an engaging social feed.

Each agent should take ONE action per turn using the post_to_site tool.
After completing 3 full cycles (each agent posting 3 times), say "TERMINATE".
    """
    print(f"🎯 MISSION: {mission}\n")

    # 7. Execution Loop
    print("🔄 Starting agent workflow...\n")
    async for event in squad.run_stream(task=mission):
        if hasattr(event, 'source') and hasattr(event, 'content'):
            content = str(event.content)

            # Hide raw tool output to keep console clean
            if isinstance(event.content, list):
                content = "[Social Feed Post Action Completed]"
            elif content is None:
                content = ""

            print(f"\n👤 [{event.source.upper()}]\n{'-' * 20}\n{content.strip()[:800]}")

            if "COMPLETE" in str(content).upper():
                print(f"\n✅ HANDOFF: {event.source.upper()} is done.")

    print(f"\n{'=' * 80}\n✨ WORKFLOW FINISHED! Check site/feed.json and run 'streamlit run site/app.py'\n{'=' * 80}")


if __name__ == "__main__":
    asyncio.run(main())
