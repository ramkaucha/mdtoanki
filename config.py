import os
from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
MODEL_NAME = "claude-3-sonnet-20240229"
MAX_TOKENS = 4000

DEFAULT_DECK_NAME = "Markdown Notes"
DEFAULT_MODEL_NAME = "Basic"
DEFAULT_CSS = """
.card {
  font-family: Arial;
  font-size: 14 px;
  text-align: left;
  color: black;
  background-color: white;
}

.question {
  font-weight: bold;
}

code {
  background-color: #f5f5f5;
  padding: 2px 4px;
  border-radius: 3px;
  font-family: monospace;
}
"""