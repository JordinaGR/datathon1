import re

def preserve_newlines_with_four_digits(text):
    pattern = re.compile(r'(?<!\d{4}\))\n')
    result = re.sub(pattern, ' ', text)
    return result

def separate_last_parenthesis(input_string):
    matches = re.findall(r'\((.*?)\)', input_string)
    
    if matches:
        content_inside_last_parenthesis = matches[-1]  # Use the last match

        # Use re.sub to remove only the last set of parentheses and its content
        modified_string = re.sub(r'\([^()]*\)$', '', input_string)

        return content_inside_last_parenthesis, modified_string

def extract_three_chars_before_min(input_string):
    match = re.search(r'(..)\b min\b', input_string)

    if match:
        three_chars_before_min = match.group(1)
        return str(three_chars_before_min).replace('(', '').replace(')', '').replace('', '')         

def extract_three_chars_before_h(input_string):
    match = re.search(r'(..)\b h\b', input_string)

    if match:
        three_chars_before_h = match.group(1)
        return str(three_chars_before_h).replace('(', '').replace(')', '').replace(' ', '')          

file_path = '/home/jordina/Desktop/datathon/dadesAuto.txt' 
with open(file_path, 'r') as file:
    file_content = file.read()

    data = preserve_newlines_with_four_digits(file_content)
    data1 = data.splitlines()
    for line_number, line in enumerate(data1, 1):
        sections = line.strip().split('&&')
        sec2, sec1 = separate_last_parenthesis(sections[1])
        # print(sections[0] + 'asdasdfasdfsdf' + sec1 +'asdf' + sec2)
        
        if sec1 not in sections[0]:
            hores_public = extract_three_chars_before_h(sections[0])
            minuts_public = extract_three_chars_before_min(sections[0])

            hores_priv = extract_three_chars_before_h(sec1)
            minuts_priv = extract_three_chars_before_min(sec1)

            temps_public = 0
            if hores_public is not None:
                temps_public += int(hores_public)*60
            if minuts_public is not None:
                temps_public += int(minuts_public)
            
            temps_privat = 0
            if hores_priv is not None:
                temps_privat += int(hores_priv)*60
            if minuts_priv is not None:
                temps_privat += int(minuts_priv)

            if temps_privat != 0 and temps_public != 0:
                diff = temps_public-temps_privat
                print(diff)
                print(sec2)
                print()

