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