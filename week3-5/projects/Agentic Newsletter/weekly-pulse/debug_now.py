import json
import pickle
import os

newsletter = None
if os.path.exists('output/latest_newsletter.pkl'):
    with open('output/latest_newsletter.pkl', 'rb') as f:
        newsletter = pickle.load(f)

if newsletter:
    for i, section in enumerate(newsletter.get('sections', [])):
        print(f"\nSection {i+1}:")
        print(f"  Header: '{section.get('header', 'MISSING')}'")
        print(f"  Category: '{section.get('category', 'MISSING')}'")
        print(f"  Intro length: {len(section.get('intro', ''))}")
        print(f"  Bullets: {len(section.get('bullets', []))}")
else:
    print("No pickle file. Let me check the HTML directly.")
    import re
    with open('output/newsletter_20260507.html', 'r', encoding='utf-8') as f:
        html = f.read()
        headers = re.findall(r'<h2[^>]*>([^<]+)</h2>', html)
        for i, h in enumerate(headers):
            print(f"Section {i+1} header: '{h}'")
