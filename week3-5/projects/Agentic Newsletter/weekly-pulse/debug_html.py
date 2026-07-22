import json
import re
from bs4 import BeautifulSoup

# Read the HTML file
with open('output/newsletter_20260507.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Parse with BeautifulSoup to see structure
soup = BeautifulSoup(html, 'html.parser')
sections = soup.find_all('div', style=re.compile(r'margin-bottom: 30px'))

print(f"Found {len(sections)} sections\n")

for i, section in enumerate(sections, 1):
    h2 = section.find('h2')
    header = h2.get_text(strip=True) if h2 else "No header"
    img = section.find('img')
    img_src = img.get('src', 'No image')[:50] if img else "No image"
    print(f"Section {i}: {header}")
    print(f"  Image: {img_src}")
    print()
