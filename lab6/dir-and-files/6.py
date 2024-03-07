import os
import string

path_to_file = './Alphabet/'

os.mkdir(path_to_file)
def generate_text_files():
    for i in range (1, 27):
        letter = chr(i + 64)
        filename = letter + ".py"
        filename = open(f'{path_to_file}{letter}', "w")
        filename.write("import string\nimport os\npath_to_file = './Alphabet/'\nos.mkdir(path_to_file)\ndef generate_text_files():\n\talphabet = string.ascii_uppercase\n\tfor letter in alphabet:\n\t\tfilename = letter + '.py'\n\t\tfilename.open(f'{path_to_file}{letter}', 'w')\n\t\tfilename.write('')")

generate_text_files()
