#!/usr/bin/env python3

import argparse
import sys
from file_handler import read_markdown_file, extract_topic_from_filename
from ai_handler import generate_cards_from_content
from anki_generator import create_anki_package
from utils import get_output_path

def main():
  """Main entry point for the app"""

  parser = argparse.ArgumentParser(description="Convert Markdown notes to Anki flashcards")
  parser.add_argument("input_file", help="Path to markdown file")
  parser.add_argument("---output", "-o", help="Output Anki package file")
  parser.add_argument("--topic", "-t", help="Topic name for the cards")
  parser.add_argument("--num", "-n", type=int, default=10, help="Number of cards to generate")

  args = parser.parse_args()

  try:
    print(f"Reading file: {args.input_file}")
    md_content = read_markdown_file(args.input_file)

    topic = args.topic
    if not topic:
      topic = extract_topic_from_filename(args.input_file)
      print(f"Using topic derived from the file name: {topic}")
    
    print(f"Generating {args.num} Anki cards from content...")
    cards = generate_cards_from_content(
      content=md_content,
      topic=topic,
      num_cards=args.num
    )

    if not cards:
      print("Error: Failed to generate cards.")
      return 1


    print(f"Successfully generated {len(cards)} cards.")

    output_file = get_output_path(args.input_file, args.output)
    create_anki_package(cards, output_file)

    print(f"Success! Created Anki package with {len(cards)} cards.")
    print(f"Output file: {output_file}")

    return 0
  except Exception as e:
    print(f"Error: {e}")
    return 1
  
if __name__ == "__main__":
  sys.exit(main())
