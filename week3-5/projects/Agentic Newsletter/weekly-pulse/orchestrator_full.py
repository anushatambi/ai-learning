"""
Full Orchestrator with HTML Email Output and Images
"""
from research_subagent import ResearchSubagent
from content_agent import ContentAgent
from media_agent import MediaAgent
from renderer import HTMLRenderer
from datetime import datetime

class FullOrchestrator:
    def __init__(self):
        print("\n🚀 Weekly Pulse Newsletter System (Full Version with Images)")
        self.researcher = ResearchSubagent()
        self.content_agent = ContentAgent()
        self.media_agent = MediaAgent()
        self.renderer = HTMLRenderer()
    
    def generate(self):
        print("\n[1/4] Gathering news...")
        articles = self.researcher.gather_all_news()
        
        print(f"\n[2/4] Creating content from {len(articles)} articles...")
        newsletter = self.content_agent.create_newsletter(articles)
        
        print("\n[3/4] Adding images to sections...")
        newsletter_with_images = self.media_agent.add_images_to_newsletter(newsletter)
        
        print("\n[4/4] Generating HTML email...")
        html_file = self.renderer.create_html(newsletter_with_images)
        
        print(f"\n✅ Complete! Open this file in your browser:")
        print(f"   {html_file}")
        return html_file

if __name__ == "__main__":
    orchestrator = FullOrchestrator()
    orchestrator.generate()