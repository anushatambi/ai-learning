from media_agent import MediaAgent

m = MediaAgent()
sections = [
    {"category": "ai_ml", "header": "AI News"},
    {"category": "dev_opensource", "header": "Dev News"},
    {"category": "industry", "header": "Industry News"}
]
newsletter = {"sections": sections}
result = m.add_images_to_newsletter(newsletter)

images = [s["image"]["url"] for s in result["sections"]]
print(f"Images used: {len(images)}")
print(f"Unique images: {len(set(images))}")
if len(images) == len(set(images)):
    print("✓ All images are unique")
else:
    print("✗ Duplicate images found")
