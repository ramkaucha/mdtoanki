import os

def ensure_file_extensions(file_path: str, extension='.apkg'):
  """ENsure the file has correct extension

  Args:
      file_path (str): Path to the file
      extension (str, optional): Desired extension. Defaults to '.apkg'.
  Returns:
      str: File path with correct extension
  """

  if not file_path.endswith(extension):
    return f"{file_path}{extension}"
  
  return file_path

def get_output_path(input_file: str, output_file=None):
  """Generate an output file path based on the input file

  Args:
      input_file (str): Path to the input file
      output_file (str, optional): Desired output path. Defaults to None.
  Returns:
      str: Output file path
  """
  if output_file:
    return ensure_file_extensions(output_file)

  base_name = os.path.basename(input_file)

  name_without_ext = os.path.splitext(base_name)[0]

  return f"{name_without_ext}.apkg"


def split_content_into_chunks(content, max_words_per_chunk=2500):
  """Split markdown content into chunks of reasonable size at logical boundaries

  Args:
      content (str): Markdown content to split
      max_words_per_chunk (int, optional): Maximum words per chunk. Defaults to 2500.
  """

  lines = content.split('\n')
  chunks = []
  current_chunk = []
  current_word_count = 0

  for line in lines:
    line_word_count = len(line.split())
    if current_word_count + line_word_count > max_words_per_chunk and current_word_count > 0:
      if line.strip().startswith('#'):
        chunks.append('\n'.join(current_chunk))
        current_chunk = [line]
        current_word_count = line_word_count
      else:
        good_break_found =  False

        for i in range(min(5, len(current_chunk))):
          if current_chunk[-(i+1)].strip().startswith('#') or not current_chunk[-(i+1)].strip():
            next_chunk_start = current_chunk[-(i+1):]
            current_chunk = current_chunk[:-(i+1)]
            chunks.append('\n'.join(current_chunk))
            current_chunk = next_chunk_start + [line]

            current_word_count = sum(len(l.split()) for l in current_chunk)
            good_break_found = True
            break


        if not good_break_found:
          chunks.append('\n'.join(current_chunk))
          current_chunk = [line]
          current_word_count = line_word_count
    else:
      current_chunk.append(line)
      current_word_count += line_word_count
  

  if current_chunk:
    chunks.append('\n'.join(current_chunk))

    return chunks