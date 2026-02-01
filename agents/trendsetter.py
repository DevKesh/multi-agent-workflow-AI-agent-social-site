from autogen_agentchat.agents import AssistantAgent
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
# noinspection PyUnresolvedReferences
from config.prompts import AgentPrompts

class TrendSetterAgent:
    def __init__(self, model_client, tool_bench=None):
        self.model_client = model_client
        self.name = "TrendSetter"
        self.tool_bench = tool_bench if tool_bench else []
        self.system_message = AgentPrompts.TRENDSETTER

    def build(self) -> AssistantAgent:
        """Creates and returns the AutoGen AssistantAgent object."""
        return AssistantAgent(
            name=self.name,
            model_client=self.model_client,
            tools=self.tool_bench,
            system_message=self.system_message
        )
