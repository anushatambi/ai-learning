import yaml
import json
import os
from datetime import datetime
import hashlib

# Load configuration
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

print("=" * 50)
print("📰 THE WEEKLY PULSE - Newsletter Generator")
print("=" * 50)
print(f"Configuration loaded successfully")
print(f"  - LLM Provider: {config['llm']['provider']}")
print(f"  - Sections: {config['newsletter']['sections']}")
print(f"  - Items per section: {config['newsletter']['items_per_section']}")
print(f"  - Total items: {config['newsletter']['sections'] * config['newsletter']['items_per_section']}")
print("=" * 50)

# This is a placeholder - full agent code will be added in next steps
print("\n✅ Project structure is ready!")
print("📁 Output folder will be created on first run")
print("🖼️ Images will be saved in output/YYYY-MM-DD/images/")
print("\nNext: Adding agent code...")