# mdtoanki

A CLI tool to convert markdown notes into Anki flashcards using the power of AI.

## Requirements
- Python 3.8+
- Anthropic API key
- Anki (to use the generated cards)


## Installation

1. Clone the repo:
```bash
git clone https://github.com/ramkaucha/mdtoanki.git
cd mdtoanki
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
```bash
- Windows: venv\Scripts\activate
- macOS/Linux: source venv/bin/activate
```

4. Install the requirements
```bash
pip install -r requirements.txt
```

5. Set up your env variables
Create a `.env` file in the project root directory with your Anthropic API key:
```
ANTHROPIC_API_KEY=your-api-key-here
```

## Usage

Basic usage:
```bash
python main.py your_notes.md
```

This will create an Anki Package(.apkg) file with the same name as your note file

### Options
- `--output`, `-o` - specify the output file path
- `--topic`, `-t` - specify the topic name (otherwise derived from the file name)
- `--num`, `-n` - number of cards to generate (default=10)

Example:
```bash
python main.py vision_notes.md --topic "Optometry" --num 15 --output vision_cards
# or
python main.py vision_notes.md --t "Optometry" --n 15 --o vision_cards
```