import re
import os

def rename_file(filename, outputname=None):
    """
    Renames a file from .ny to .py or adds .py if not present.
    """
    if outputname is not None:
        return outputname
    if filename.endswith('.ny'):
        return filename[:-3] + '.py'
    else:
        return filename + '.py'

def parse_imports(filename):
    """
    Parses a file for import statements and returns a list of imported modules with '.ny' suffix.
    """
    with open(filename, 'r') as file:
        content = file.read()
    imports = re.findall(r"(?<=import\s)[\w.]+(?=;|\s|$)", content)
    imports += re.findall(r"(?<=from\s)[\w.]+(?=\s+import)", content)
    return [im + ".ny" for im in imports]

def convert_syntax(filepath, outputname=None):
    """
    Converts basic Nython syntax to Python syntax and writes the result to a new file.
    """
    filename = os.path.basename(filepath)
    new_filename = rename_file(filename, outputname)
    with open(filepath, 'r') as infile, open(new_filename, 'w') as outfile:
        for line in infile:
            # Convert basic syntax here
            # For example, replace '{}' with ':' and remove '}'
            line = line.replace('{', ':').replace('}', '')
            outfile.write(line)

# # Example usage
# filepath = 'test.ny'
# convert_syntax(filepath)
