import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from reportlab.pdfgen.canvas import Canvas

whitelist = ['p']

url = 'https://kisslightnovels.info/novel/battle-through-the-heavens-light-novel-free/battle-through-the-heavens-chapter-'
for chapter_num in range(1, 3):
    response = requests.get(f'{url}{chapter_num}/')
    soup = BeautifulSoup(response.text, "html.parser")

    # Get all p tags as text.
    text_elements = [t for t in soup.find_all(text=True) if t.parent.name in whitelist]
    endpoint = len(text_elements) - 26

    text_elements = text_elements[2:endpoint]
    chapter_name = text_elements[0].replace(':', ' -')

    # for index, value in enumerate(text_elements):
        # print(f'{index} === {value}')

    time.sleep(1)

# Create the pdf
# canvas = Canvas(chapter_name)
