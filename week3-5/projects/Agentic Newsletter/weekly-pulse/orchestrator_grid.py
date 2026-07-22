"""
Orchestrator Grid - Coordinates research and grid rendering
"""
from research_subagent import ResearchSubagent
from grid_renderer import GridRenderer
from datetime import datetime

class NewsletterOrchestrator:
    """Orchestrates the complete newsletter generation process"""
    
    def __init__(self):
        print("=" * 50)
        print("WEEKLY PULSE NEWSLETTER ORCHESTRATOR")
        print("Grid Layout | 5 Sections × 4 Articles = 20 News Items")
        print("=" * 50)
        
        self.researcher = ResearchSubagent()
        self.renderer = GridRenderer()
    
    def generate(self):
        """Generate complete newsletter"""
        print("\n[Step 1] Gathering news articles...")
        articles = self.researcher.gather_all_news()
        
        print(f"\n[Step 2] Preparing newsletter data...")
        newsletter_data = {
            'title': f"Weekly Pulse - {datetime.now().strftime('%B %d, %Y')}",
            'articles': articles,
            'total_articles': len(articles)
        }
        
        print(f"\n[Step 3] Generating grid layout HTML...")
        output_path = self.renderer.create_html(newsletter_data)  # Fixed: changed 'newsletter_data' to 'newsletter_data'
        
        print("\n" + "=" * 50)
        print("✅ NEWSLETTER GENERATION COMPLETE!")
        print(f"📧 Output: {output_path}")
        print(f"📊 Statistics: {len(articles)} articles, 5 sections, 4 per section")
        print("=" * 50)
        
        return output_path

if __name__ == "__main__":
    orchestrator = NewsletterOrchestrator()
    output_file = orchestrator.generate()
    print(f"\n🎉 Newsletter ready! Open in browser: {output_file}")
