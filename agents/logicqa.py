from autogen_agentchat.agents import AssistantAgent
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
# noinspection PyUnresolvedReferences
from config.prompts import AgentPrompts


class LogicQAAgent:
    """
    Factory for creating an AutoGen ``AssistantAgent`` configured for logic and
    question-answering tasks.

    This class wraps the configuration required to build an ``AssistantAgent``,
    including the underlying model client, any tool integrations, and the
    system prompt used to steer the agent's behavior. Typical usage is:

        logic_agent = LogicQAAgent(model_client, tool_bench=[...])
        assistant = logic_agent.build()

    Parameters
    ----------
    model_client :
        The model client instance used by the underlying ``AssistantAgent`` to
        generate responses.
    tool_bench : list, optional
        A collection of tool specifications or tool instances that the
        ``AssistantAgent`` can invoke while answering questions. If ``None``,
        an empty tool list is used.
    """

    def __init__(self, model_client, tool_bench=None):
        self.model_client = model_client
        self.name = "LogicQA"
        self.tool_bench = tool_bench if tool_bench is not None else []
        self.system_message = AgentPrompts.LOGICQA

    def build(self) -> AssistantAgent:
        """Creates and returns the AutoGen AssistantAgent object."""
        return AssistantAgent(
            name=self.name,
            model_client=self.model_client,
            tools=self.tool_bench,
            system_message=self.system_message
        )
