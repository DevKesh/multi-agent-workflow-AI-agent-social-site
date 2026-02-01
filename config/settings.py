import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
api_key = os.getenv("OPENAI_API_KEY", "your-api-key-here")
model_name = os.getenv("MODEL_NAME", "gpt-4o")

# Site Configuration
FEED_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'site', 'feed.json')
