"""
Orchestrator - Main controller for Weekly Pulse Newsletter
"""
from research_subagent import ResearchSubagent
from content_agent import ContentAgent
from datetime import datetime
import json

class Orchestrator:
    """Main orchestrator that runs the complete newsletter pipeline"""
    
    def __init__(self):
        print("=" * 50)
        print("WEEKLY PULSE NEWSLETTER ORCHESTRATOR")
        print("=" * 50)
        self.researcher = ResearchSubagent()
        self.content_agent = ContentAgent()
    
    def generate_newsletter(self):
        """Run the complete newsletter generation pipeline"""
        
        print("\n[STEP 1] Gathering news from all sources...")
        articles = self.researcher.gather_all_news()
        
        if not articles:
            print("ERROR: No articles found!")
            return None
        
        print(f"\n[STEP 2] Creating newsletter content with AI...")
        newsletter = self.content_agent.create_newsletter(articles)
        
        print(f"\n[STEP 3] Saving newsletter...")
        
        # Save to file
        filename = f"output/newsletter_{datetime.now().strftime('%Y%m%d')}.txt"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("=" * 60 + "\n")
            f.write(newsletter['title'] + "\n")
            f.write("=" * 60 + "\n\n")
            
            for section in newsletter['sections']:
                f.write(f"\n## {section['header']}\n")
                f.write(f"{section['intro']}\n\n")
                for bullet in section['bullets']:
                    f.write(f"  • {bullet}\n")
                f.write("\n" + "-" * 40 + "\n")
        
        print(f"\n✓ Newsletter saved to: {filename}")
        
        # Print preview
        print("\n" + "=" * 50)
        print("PREVIEW (first 3 sections)")
        print("=" * 50)
        for section in newsletter['sections'][:3]:
            print(f"\n📰 {section['header']}")
            print(f"   {section['intro'][:100]}...")
        
        return filename
    
    def run_weekly(self):
        """Weekly run with timestamp"""
        print(f"\nStarting weekly run at {datetime.now()}")
        result = self.generate_newsletter()
        print(f"\n✓ Weekly run complete at {datetime.now()}")
        return result

# Run the orchestrator
if __name__ == "__main__":
    print("\n🚀 Starting Weekly Pulse Newsletter System...\n")
    orchestrator = Orchestrator()
    output_file = orchestrator.run_weekly()
    
    if output_file:
        print(f"\n✅ SUCCESS! Newsletter generated: {output_file}")
        print("\n📧 Ready for sending or publishing")
    else:
        print("\n❌ FAILED: Newsletter generation encountered errors")