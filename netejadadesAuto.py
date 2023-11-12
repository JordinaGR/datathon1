import re

def preserve_newlines_with_four_digits(text):
    pattern = re.compile(r'(?<!\d{4}\))\n')
    result = re.sub(pattern, ' ', text)
    return result

file_path = '/home/jordina/Desktop/datathon/dadesAuto.txt' 
with open(file_path, 'r') as file:
    file_content = file.read()

    data = preserve_newlines_with_four_digits(file_content)

