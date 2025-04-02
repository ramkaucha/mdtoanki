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
    Please analyze the following notes on {topic or 'the given topic'} and create {num_cards} Anki flashcards.

    For each card:
    1. Generate a clear, specific question that tests understanding
    2. Provide a comprehensive answer/explanation
    3. Format code, lists, and important terms appropriately

    Return the results as a JSON array with objects containing 'question' and 'answer' fields.

    NOTES:
    {content}
    """

    res = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=4000,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    # raw_res = res.content[0].text
    # print("\nRaw API Response:")
    # print("-" * 50)
    # print(raw_res)
    # print("-" * 50)

    ai_res = res.content[0].text

    try:
        print("\Trying regex extraction...")
        json_match = re.search(r'\[\s*\{.*\}\s*\]', ai_res, re.DOTALL)
        if json_match:
            print("JSON pattern found")
            cards = json.loads(json_match.group(0))
            return cards
        else:
            print("NO json pattern found")
            cards = json.loads(ai_res)
        return cards
    except json.JSONDecodeError:
        print("Failed to parse JSON from response")
        return []