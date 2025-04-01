import os
import markdown

def read_markdown_file(file_path: str):
  """Read and return the content of a markdown file

  Args:
      file_path (str): Path to the markdown file
  
  Returns:
      str: Content of the markdown file
  
  Raises:
      FileNotFoundError: If the file is not found
  """

  if not os.path.exists(file_path):
    raise FileNotFoundError(f"File not found: {file_path}")
  
  with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
  

  return content

def extract_topic_from_filename(file_path: str):
  """Extract a topic name from the filename

  Args:
      file_path (str): Path to the file
  Returns:
      str: Topic name derived from filename
  """

  base_name = os.path.basename(file_path)

  topic = os.path.splitext(base_name)[0].replace('_', ' ').replace('-', ' ')

  return topic.title()