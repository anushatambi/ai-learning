"""
Content Agent - Generates newsletter sections using Ollama LLM
"""
import ollama
import json
import re
from datetime import datetime

class ContentAgent:
    """Creates engaging newsletter content using Llama 3.2"""
    
    def __init__(self):
        print("Content Agent initialized")
        self.model = "llama3.2:3b"
    
    def create_newsletter(self, articles):
        """Generate complete newsletter from articles"""
        print(f"Creating newsletter from {len(articles)} articles...")
        
        # Group articles by category
        grouped = {}
        for article in articles:
            cat = article.get('section', 'general')
            if cat not in grouped:
                grouped[cat] = []
            if len(grouped[cat]) < 3:  # Max 3 per section
                grouped[cat].append(article)
        
        sections = []
        
        for category, cat_articles in grouped.items():
            section = self.create_section(category, cat_articles)
            sections.append(section)
            print(f"  Created section: {category}")
        
        return {
            'title': f"Weekly Pulse - {datetime.now().strftime('%B %d, %Y')}",
            'sections': sections,
            'total_articles': len(articles)
        }
    
    def clean_header(self, raw_header, category):
        """Clean up header by removing ALL prefixes and formatting properly"""
        if not raw_header:
            return self.format_category_name(category)
        
        # Convert to string and clean
        raw_header = str(raw_header)
        
        # Remove ALL patterns like "section2 : ", "section 2 - ", "Section 2:", etc.
        patterns = [
            r'^[Ss]ection\s*\d+\s*[:._\-–—]*\s*',  # Section 1: Section1: Section 2- etc
            r'^[Ss]ection\s*\d+\s+',                # Section 2 
            r'^\d+[:._\-–—]*\s*',                   # 1: 1. 1- etc
            r'^[Ss]ection\s*',                      # Section (alone)
            r'^[Ss]ection\s*\d+\s*:\s*',           # section2 : (with space before colon)
            r'^[Ss]ection\s*\d+\s+-\s+',           # section2 - (with hyphen)
        ]
        
        for pattern in patterns:
            raw_header = re.sub(pattern, '', raw_header)
        
        # Clean up spacing and special characters
        raw_header = ' '.join(raw_header.split())
        raw_header = raw_header.strip(' :._-–—')
        raw_header = raw_header.strip()  # Final trim
        
        # Additional check: if header starts with lowercase, capitalize first letter
        if raw_header and raw_header[0].islower():
            raw_header = raw_header[0].upper() + raw_header[1:]
        
        # If header is empty or too short, use formatted category
        if len(raw_header) < 3:
            return self.format_category_name(category)
        
        return raw_header
    
    def format_category_name(self, category):
        """Format category names nicely"""
        category_map = {
            'ai_ml': 'AI & ML News',
            'dev_opensource': 'Open Source Development',
            'industry': 'Industry News',
            'hackathon': 'Hackathon Update',
            'datascience': 'Data Science News',
            'general': 'Weekly Update'
        }
        
        # Check if category matches any key
        for key, value in category_map.items():
            if key in category.lower() or category.lower() in key:
                return value
        
        # Default: replace underscores and title case
        return category.replace('_', ' ').title()
    
    def create_section(self, category, articles):
        """Create one section using LLM"""
        
        # Prepare articles summary
        articles_text = ""
        for a in articles:
            articles_text += f"\n- {a['title']}\n  {a['summary'][:150]}...\n"
        
        prompt = f"""You write a newsletter section about {category}.

Here are the news articles:
{articles_text}

Write a short section with:
1. A short, clean header (just the topic name, no "Section" prefixes, under 40 chars)
2. One paragraph intro (2-3 sentences)
3. Three bullet points with key insights

IMPORTANT: 
- Header should be simple like "AI Breakthroughs" or "Open Source Updates"
- Do NOT include "Section 1" or any numbering in the header
- Return ONLY valid JSON. Use double quotes. No trailing commas.

Example format: {{"header":"AI Breakthroughs", "intro":"This week saw major advances in artificial intelligence.", "bullets":["First key insight","Second important finding","Third major development"]}}

Return ONLY valid JSON:
{{"header":"...", "intro":"...", "bullets":["...","...","..."]}}
"""
        
        try:
            response = ollama.chat(model=self.model, messages=[
                {'role': 'user', 'content': prompt}
            ])
            
            # Parse JSON response
            result = json.loads(response['message']['content'])
            
            # Clean up the header
            clean_header = self.clean_header(result.get('header', ''), category)
            
            return {
                'category': category,
                'header': clean_header,
                'intro': result.get('intro', 'Key developments this week'),
                'bullets': result.get('bullets', ['Read the full article for details']),
                'articles': articles,
                'article_links': [{'title': a['title'], 'url': a.get('url', '#'), 'summary': a.get('summary', '')[:100]} for a in articles]
            }
        except Exception as e:
            print(f"  LLM error for {category}: {e}")
            print(f"  Response was: {response['message']['content'][:200] if 'response' in locals() else 'No response'}")
            # Fallback without LLM
            clean_header = self.clean_header('', category)
            return {
                'category': category,
                'header': clean_header,
                'intro': f'Latest developments in {category.replace("_", " ")} this week.',
                'bullets': [articles[0]['title'][:100] if articles else 'No articles available'],
                'articles': articles,
                'article_links': [{'title': a['title'], 'url': a.get('url', '#'), 'summary': a.get('summary', '')[:100]} for a in articles[:3]]
            }


# Quick test
if __name__ == "__main__":
    # Test with sample articles
    test_articles = [
        {'title': 'AI Breakthrough Announced', 'summary': 'New model beats all benchmarks', 'section': 'ai_ml'},
        {'title': 'Open Source Library Released', 'summary': 'New tool for developers', 'section': 'dev_opensource'},
        {'title': 'Startup Raises $50M', 'summary': 'Series B funding round closes', 'section': 'industry'}
    ]
    
    agent = ContentAgent()
    newsletter = agent.create_newsletter(test_articles)
    
    print(f"\n--- NEWSLETTER: {newsletter['title']} ---")
    for section in newsletter['sections']:
        print(f"\n## {section['header']}")
        print(f"{section['intro']}")
        for bullet in section['bullets']:
            print(f"  • {bullet}")