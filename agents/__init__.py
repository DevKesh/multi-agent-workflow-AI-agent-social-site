import sys
import os

# Add parent directory to Python path
_parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _parent_dir not in sys.path:
    sys.path.insert(0, _parent_dir)

from agents.trendsetter import TrendSetterAgent
from agents.newsbreaker import NewsBreakerAgent
from agents.logicqa import LogicQAAgent

__all__ = ["TrendSetterAgent", "NewsBreakerAgent", "LogicQAAgent"]
