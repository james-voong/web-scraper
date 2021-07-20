import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from reportlab.pdfgen.canvas import Canvas

url = 'https://novelfull.com/battle-through-the-heavens/chapter-1-genius-no-more.html'
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

whitelist = [
  'p'
]

# Get all p tags as text.
text_elements = [t for t in soup.find_all(text=True) if t.parent.name in whitelist]

endpoint = len(text_elements) - 1
text_elements = text_elements[0:endpoint]

# Split the chapter name string.
raw_chapter_name = text_elements[0].split()

# Insert a - at position 2
raw_chapter_name.insert(2, '-')

# Convert the array to a string, separated by whitespace.
chapter_name = ' '.join(raw_chapter_name)

# Create the pdf
canvas = Canvas(chapter_name)
