from renderer import HTMLRenderer

r = HTMLRenderer()
test_data = {
    "sections": [{
        "header": "Test",
        "intro": "Test intro",
        "bullets": ["Bullet 1", "Bullet 2"],
        "article_links": [{"title": "Test Article", "url": "#", "summary": "Test"}]
    }]
}
output = r.create_html(test_data, "output/test.html")
print(f"HTML saved to: {output}")
