"""Function for creating Anki packages."""

import genanki
import random
from typing import List, Dict
from config import DEFAULT_DECK_NAME, DEFAULT_MODEL_NAME, DEFAULT_CSS

def create_anki_model(name=DEFAULT_MODEL_NAME):
  """Create an Anki note model

  Args:
      name (_type_, optional): Name for the model. Defaults to DEFAULT_MODEL_NAME.

  Returns:
      genanki.Model: Anki note model
  """

  model_id = random.randrange(1 << 30, 1 << 31)

  model = genanki.Model(
    model_id,
    name,
    fields=[
      { 'name': 'Question' },
      { 'name': 'Answer' }
    ],
    templates=[
      {
        'name': 'Card 1',
        'qfmt': '<div class="question">{{Question}}</div>',
        'afmt': '<div class="answer">>{{Answer}}</div>'
      },
    ],
    css=DEFAULT_CSS
  )

  return model

def create_anki_package(
    cards: List[Dict[str, str]],
    output_file: str,
    topic: str = None):
  """Create an Anki package file from a list of cards

  Args:
      cards (List[Dict[str, str]]): List of dicts with questions and answer fields
      output_file (str): Output file path
      topic (str, optional): Topic name for the deck. Defaults to None.
  Returns:
      str: Path to the created Anki package
  """

  model = create_anki_model()

  deck_name = topic or DEFAULT_DECK_NAME
  deck_id = random.randrange(1 << 30, 1 << 31)
  deck = genanki.Deck(deck_id, deck_name)

  for card in cards:
    note = genanki.Note(
      model=model,
      fields=[card['question'], card['answer']]
    )
    deck.add_note(note)

  package = genanki.Package(deck)

  package.write_to_file(output_file)

  return output_file