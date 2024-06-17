import pdfplumber
import re

def replace_consecutive_spaces(text):
    # Replace more than two consecutive spaces with a single space
    return re.sub(r'\s{2,}', ' ', text)


pdf = pdfplumber.open('strategy.pdf')

print(len(pdf.pages))

text = ""
for i in range(len(pdf.pages)):
    page = pdf.pages[i]
    text_a = page.extract_text()
    text = text +" "+ replace_consecutive_spaces(text_a.replace("\n"," "))

print(text)

file_path = 'strategy.md'

# Writing to the file
with open(file_path, 'w') as file:
    file.write(text)

pdf.close()