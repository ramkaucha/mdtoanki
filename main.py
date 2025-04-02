#!/usr/bin/env python3

import argparse
import sys
from file_handler import read_markdown_file, extract_topic_from_filename
from ai_handler import generate_cards_from_content
from anki_generator import create_anki_package
from utils import get_output_path, split_content_into_chunks

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

    word_count = len(md_content.split())
    print(f"Content has approximately {word_count} words")

    max_chunk_size = 2500
    tolerance =  500

    all_cards = []

    if word_count <= max_chunk_size + tolerance:
      print(f"Generating {args.num} Anki cards from content...")
      all_cards = generate_cards_from_content(
        content=md_content,
        topic=topic,
        num_cards=args.num
      )
    else:
      chunks = split_content_into_chunks(md_content, max_chunk_size)
      total_cards = args.num
      cards_per_chunk = [max(1, int(total_cards * (len(chunk.split()) / word_count))) for chunk in chunks]

      while sum(cards_per_chunk) < total_cards:
        cards_per_chunk[0] += 1
      
      print(f"Content will be processed in {len(chunks)} chunks")

      for i, (chunk, num_cards) in enumerate(zip(chunks, cards_per_chunk), 1):
        if num_cards == 0:
          continue

        print(f"Processing chunk {i}/{len(chunks)}, generating {num_cards} cards...")
        chunk_cards = generate_cards_from_content(
          content=chunk,
          topic=f"{topic} (Part {i})",
          num_cards=num_cards
        )

        all_cards.extend(chunk_cards)

    if not all_cards:
      print("Error: Failed to generate cards.")
      return 1


    print(f"Successfully generated {len(all_cards)} cards.")

    output_file = get_output_path(args.input_file, args.output)
    create_anki_package(all_cards, output_file)

    print(f"Success! Created Anki package with {len(all_cards)} cards.")
    print(f"Output file: {output_file}")

    return 0
  except Exception as e:
    print(f"Error: {e}")
    return 1
if __name__ == "__main__":
  sys.exit(main())
