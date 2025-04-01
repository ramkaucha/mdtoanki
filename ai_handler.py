import os
from anthropic import Anthropic
from typing import List, Dict
import json
import re

def generate_cards_from_content(
    content: str,
    topic: str = None,
    num_cards: int = 10) -> List[Dict[str, str]]:
  """Send content to the API and get back structured anki cards

  Args:
      content (str): The markdown content to process
      topic (str, optional): Topic name to focus the AI. Defaults to None.
      num_cards (int, optional): Number of cards to generate. Defaults to 10.

  Returns:
      List[Dict[str, str]]: List of dictionaries with question and answer pairs
  """

  client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

  prompt = f"""
  Please analyse the following notes { topic or 'the given topic' } and create {num_cards} Anki flashcards.

  For each card:
  1. Generate a clear, specific question that tests understanding
  2. Provide a comprehensive answer/explanation
  3. Format code, lists, and important terms appropriately

  Return the results as a JSON array with objects containing 'questions' and 'answer' fields.

  NOTES:
  {content}
  """

  res = client.messages.create(
    model="claude-3-sonnet-20240229",
    max_tokens=4000,
    messages=[
      { "role": "user", "content": prompt }
    ]
  )

  ai_res = res.content[0].text

  try:
    json_match = re.search(r'\[\s*\{.*\}\s*\]', ai_res, re.DOTALL)

    if json_match:
      cards = json.loads(json_match.group(0))
    else:
      cards = json.loads(ai_res)
    return cards
  except json.JSONDecodeError:
    print("Failed to parse JSON from response")

    return []