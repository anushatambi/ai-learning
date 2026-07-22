from content_agent import ContentAgent

c = ContentAgent()
test_articles = [{
    "title": "Test",
    "summary": "This is a test summary for the article that should be reasonably long to simulate real content",
    "section": "ai_ml",
    "url": "https://test.com"
}]

result = c.create_section("ai_ml", [test_articles[0]])
print(f"Header: {result['header']}")
print(f"Intro: {result['intro'][:50]}...")
print(f"Bullets: {len(result['bullets'])}")
