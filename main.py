import requests
from bs4 import BeautifulSoup
from fpdf import FPDF

whitelist = ['p']

url = 'https://kisslightnovels.info/novel/battle-through-the-heavens-light-novel-free/battle-through-the-heavens-chapter-'
start_chapter = 1
end_chapter = 1649

# How many lines to trim from the start and end.
start_cut = 2
end_cut = 26

test = False

for chapter_num in range(start_chapter, end_chapter):
    response = requests.get(f'{url}{chapter_num}/')
    soup = BeautifulSoup(response.text, "html.parser")

    # Get all p tags as text.
    text_elements = [t for t in soup.find_all(text=True) if t.parent.name in whitelist]
    endpoint = len(text_elements) - end_cut

    if test:
        for index, value in enumerate(text_elements):
            print(f'[{index}] {value}')

    text_elements = text_elements[start_cut:endpoint]
    chapter_name = text_elements[0].replace(':', ' -')

    pdf = FPDF()
    pdf.add_page()

    pdf.add_font('ArialUnicode', '', 'arial-unicode-ms.ttf', uni=True)
    pdf.add_font('ArialUnicode', 'B', 'arial-unicode-ms-bold.ttf', uni=True)
    pdf.set_font('ArialUnicode', '', 11)

    for index, value in enumerate(text_elements):
        if index == 0:
            pdf.set_font('ArialUnicode', 'B', 13)
            pdf.write(5, value+'\n\n')
            pdf.set_font('ArialUnicode', '', 11)
            continue

        pdf.write(5, value+'\n\n')

    pdf.output(f"{chapter_name}.pdf")