from research_subagent import ResearchSubagent
r = ResearchSubagent()
articles = r.fetch_articles("ai_ml", 1)
print(f"Summary length: {len(articles[0]['summary'].split())} words")
print("-" * 50)
print(articles[0]["summary"])
