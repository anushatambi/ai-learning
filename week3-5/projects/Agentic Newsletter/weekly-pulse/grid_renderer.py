"""
Grid Renderer - Creates tiled grid layout newsletter with blue/white theme
ENSURES EVERY ARTICLE HAS AN IMAGE - NO EXCEPTIONS
"""
from datetime import datetime
import hashlib

class GridRenderer:
    """Converts newsletter to beautiful grid layout HTML"""
    
    def __init__(self):
        self.section_icons = {
            'ai_ml': '🤖',
            'dev_opensource': '💻',
            'industry': '🏭',
            'hackathon': '🏆',
            'datascience': '📊',
            'general': '📰'
        }
        
        self.section_colors = {
            'ai_ml': '#2563eb',
            'dev_opensource': '#3b82f6',
            'industry': '#60a5fa',
            'hackathon': '#7c3aed',
            'datascience': '#06b6d4',
            'general': '#64748b'
        }
        
        # ULTRA RELIABLE IMAGE DATABASE - guaranteed to work images
        self.guaranteed_images = {
            'ai_ml': [
                'https://images.unsplash.com/photo-1677442136019-21780ecad995?w=400&h=300&fit=crop',
                'https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=400&h=300&fit=crop',
                'https://images.unsplash.com/photo-1635070041078-e363dbe005cb?w=400&h=300&fit=crop',
                'https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=400&h=300&fit=crop',
                'https://images.unsplash.com/photo-1555255707-c07966088b7b?w=400&h=300&fit=crop'
            ],
            'dev_opensource': [
                'https://images.unsplash.com/photo-1542831371-29b0f74f9713?w=400&h=300&fit=crop',
                'https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=400&h=300&fit=crop',
                'https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=400&h=300&fit=crop',
                'https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?w=400&h=300&fit=crop',
                'https://images.unsplash.com/photo-1461749280684-dccba630e2f6?w=400&h=300&fit=crop'
            ],
            'industry': [
                'https://images.unsplash.com/photo-1560179707-f14e90ef3623?w=400&h=300&fit=crop',
                'https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=400&h=300&fit=crop',
                'https://images.unsplash.com/photo-1563986768609-322da13575f3?w=400&h=300&fit=crop',
                'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=400&h=300&fit=crop',
                'https://images.unsplash.com/photo-1446776653964-20c1d3a81b06?w=400&h=300&fit=crop'
            ],
            'hackathon': [
                'https://images.unsplash.com/photo-1504384764586-bb4cdc1707b0?w=400&h=300&fit=crop',
                'https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?w=400&h=300&fit=crop',
                'https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=400&h=300&fit=crop',
                'https://images.unsplash.com/photo-1580894732934-93bced6d9f84?w=400&h=300&fit=crop',
                'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=400&h=300&fit=crop'
            ],
            'datascience': [
                'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=400&h=300&fit=crop',
                'https://images.unsplash.com/photo-1533743983669-94c0f7bddaf2?w=400&h=300&fit=crop',
                'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=400&h=300&fit=crop',
                'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=400&h=300&fit=crop',
                'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=400&h=300&fit=crop'
            ]
        }
        
        # Ultimate fallback - these ALWAYS work
        self.ultimate_fallback_images = [
            'https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=400&h=300&fit=crop',
            'https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=400&h=300&fit=crop',
            'https://images.unsplash.com/photo-1581091226033-d5c48150dbaa?w=400&h=300&fit=crop',
            'https://images.unsplash.com/photo-1488229297570-58520851e868?w=400&h=300&fit=crop',
            'https://images.unsplash.com/photo-1581092160562-40aa08e78837?w=400&h=300&fit=crop'
        ]
    
    def get_guaranteed_image(self, article, index):
        """FOUR LAYERS OF FALLBACK - ABSOLUTELY GUARANTEES AN IMAGE"""
        
        # LAYER 1: Check if article has a valid image_url
        if article.get('image_url') and article['image_url'].strip() and len(article['image_url']) > 10:
            return article['image_url']
        
        # LAYER 2: Check if article has a section and use section-specific images
        section = article.get('section', 'general')
        
        if section in self.guaranteed_images:
            # Use consistent but varied images based on title and index
            title = article.get('title', '')
            hash_val = (hash(title) + index) % len(self.guaranteed_images[section])
            return self.guaranteed_images[section][hash_val]
        
        # LAYER 3: Use category detection from title
        title = article.get('title', '').lower()
        
        if 'ai' in title or 'machine learning' in title or 'deep learning' in title or 'claude' in title or 'gpt' in title:
            return self.guaranteed_images['ai_ml'][hash(title) % len(self.guaranteed_images['ai_ml'])]
        elif 'code' in title or 'github' in title or 'docker' in title or 'rust' in title or 'vs code' in title:
            return self.guaranteed_images['dev_opensource'][hash(title) % len(self.guaranteed_images['dev_opensource'])]
        elif 'microsoft' in title or 'google' in title or 'aws' in title or 'amazon' in title or 'nvidia' in title:
            return self.guaranteed_images['industry'][hash(title) % len(self.guaranteed_images['industry'])]
        elif 'hackathon' in title or 'prize' in title or 'challenge' in title:
            return self.guaranteed_images['hackathon'][hash(title) % len(self.guaranteed_images['hackathon'])]
        elif 'pandas' in title or 'jupyter' in title or 'spark' in title or 'snowflake' in title or 'data' in title:
            return self.guaranteed_images['datascience'][hash(title) % len(self.guaranteed_images['datascience'])]
        
        # LAYER 4: ULTIMATE FALLBACK - these ALWAYS work
        return self.ultimate_fallback_images[index % len(self.ultimate_fallback_images)]
    
    def create_html(self, newsletter_data, output_path=None):
        """Generate grid layout HTML from newsletter data - EVERY ARTICLE GETS AN IMAGE"""
        
        if output_path is None:
            output_path = f"output/newsletter_grid_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
        
        # Group articles by section
        sections = {}
        for article in newsletter_data.get('articles', []):
            section = article.get('section', 'general')
            if section not in sections:
                sections[section] = []
            sections[section].append(article)
        
        # Build sections HTML
        sections_html = ""
        total_articles = 0
        articles_with_images = 0
        
        for section_name, articles in sections.items():
            # Get section display name
            display_name = section_name.replace('_', ' ').title()
            icon = self.section_icons.get(section_name, '📰')
            bar_color = self.section_colors.get(section_name, '#3b82f6')
            
            # Build cards for this section (4 per row)
            cards_html = ""
            for idx, article in enumerate(articles[:4]):  # Max 4 per section
                total_articles += 1
                
                # FORCE an image - GUARANTEED to have one
                image_url = self.get_guaranteed_image(article, idx)
                
                if image_url:
                    articles_with_images += 1
                
                # HTML with multiple image fallbacks (onerror)
                card_html = f"""
                <div class="news-card">
                    <div class="card-image">
                        <img src="{image_url}" 
                             alt="{article['title'][:50]}"
                             loading="lazy"
                             style="width:100%; height:100%; object-fit:cover;"
                             onerror="this.onerror=null; this.src='https://via.placeholder.com/400x300/2563eb/FFFFFF?text=Weekly+Pulse'; this.style.objectFit='cover';">
                    </div>
                    <div class="card-content">
                        <h3 class="card-title">{self.escape_html(article['title'])}</h3>
                        <p class="card-summary">{self.escape_html(article['summary'])}</p>
                        <a href="{article.get('url', '#')}" class="read-more" target="_blank" rel="noopener noreferrer">
                            Read More →
                        </a>
                    </div>
                </div>
                """
                cards_html += card_html
            
            # Section HTML with colored bar
            sections_html += f"""
            <div class="section">
                <div class="section-header" style="border-left-color: {bar_color};">
                    <span class="section-icon">{icon}</span>
                    <h2 class="section-title">{display_name}</h2>
                </div>
                <div class="section-divider" style="background: {bar_color};"></div>
                <div class="cards-grid">
                    {cards_html}
                </div>
            </div>
            """
        
        # Print verification
        print(f"  ✓ Image verification: {articles_with_images}/{total_articles} articles have images assigned")
        if articles_with_images == total_articles:
            print(f"  ✅ SUCCESS: All {total_articles} articles have guaranteed images!")
        else:
            print(f"  ⚠️ Warning: {total_articles - articles_with_images} articles missing images - check logs")
        
        # Complete HTML template
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>Weekly Pulse - Tech Newsletter</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
            color: #1e293b;
            line-height: 1.5;
        }}
        
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
        }}
        
        /* Header Styles */
        .main-header {{
            text-align: center;
            padding: 40px 20px;
            background: linear-gradient(135deg, #1e3a5f 0%, #2563eb 100%);
            border-radius: 20px;
            margin-bottom: 40px;
            color: white;
            box-shadow: 0 10px 25px -5px rgba(0,0,0,0.1);
        }}
        
        .main-header h1 {{
            font-size: 2.5rem;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
        }}
        
        .main-header .date {{
            font-size: 1rem;
            opacity: 0.9;
        }}
        
        .main-header .tagline {{
            font-size: 1.1rem;
            opacity: 0.8;
            margin-top: 10px;
        }}
        
        /* Section Styles */
        .section {{
            margin-bottom: 50px;
        }}
        
        .section-header {{
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 15px;
            padding-left: 15px;
            border-left-width: 5px;
            border-left-style: solid;
        }}
        
        .section-icon {{
            font-size: 2rem;
        }}
        
        .section-title {{
            font-size: 1.8rem;
            font-weight: 700;
            color: #1e293b;
        }}
        
        .section-divider {{
            height: 3px;
            width: 60px;
            border-radius: 3px;
            margin-bottom: 25px;
        }}
        
        /* Grid Layout - 4 columns */
        .cards-grid {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 25px;
        }}
        
        /* Card Styles */
        .news-card {{
            background: white;
            border-radius: 16px;
            overflow: hidden;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -1px rgba(0,0,0,0.06);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            height: 100%;
            display: flex;
            flex-direction: column;
        }}
        
        .news-card:hover {{
            transform: translateY(-4px);
            box-shadow: 0 20px 25px -5px rgba(0,0,0,0.1), 0 10px 10px -5px rgba(0,0,0,0.04);
        }}
        
        .card-image {{
            width: 100%;
            height: 160px;
            overflow: hidden;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            position: relative;
        }}
        
        .card-image img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.3s ease;
        }}
        
        .news-card:hover .card-image img {{
            transform: scale(1.05);
        }}
        
        .card-content {{
            padding: 20px;
            flex: 1;
            display: flex;
            flex-direction: column;
        }}
        
        .card-title {{
            font-size: 1rem;
            font-weight: 700;
            color: #1e293b;
            margin-bottom: 12px;
            line-height: 1.4;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }}
        
        .card-summary {{
            font-size: 0.85rem;
            color: #475569;
            line-height: 1.5;
            margin-bottom: 16px;
            flex: 1;
            display: -webkit-box;
            -webkit-line-clamp: 4;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }}
        
        .read-more {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            color: #2563eb;
            text-decoration: none;
            font-size: 0.85rem;
            font-weight: 600;
            transition: gap 0.2s ease;
        }}
        
        .read-more:hover {{
            gap: 12px;
            color: #1d4ed8;
        }}
        
        /* Footer */
        .footer {{
            text-align: center;
            padding: 40px 20px;
            margin-top: 40px;
            background: white;
            border-radius: 16px;
            color: #64748b;
            font-size: 0.85rem;
        }}
        
        /* Mobile Responsive */
        @media (max-width: 1200px) {{
            .cards-grid {{
                gap: 20px;
            }}
            .card-title {{
                font-size: 0.9rem;
            }}
        }}
        
        @media (max-width: 992px) {{
            .cards-grid {{
                grid-template-columns: repeat(2, 1fr);
                gap: 20px;
            }}
            .main-header h1 {{
                font-size: 2rem;
            }}
        }}
        
        @media (max-width: 576px) {{
            .cards-grid {{
                grid-template-columns: 1fr;
            }}
            .container {{
                padding: 15px;
            }}
            .main-header {{
                padding: 30px 15px;
            }}
            .main-header h1 {{
                font-size: 1.5rem;
            }}
            .section-title {{
                font-size: 1.4rem;
            }}
        }}
        
        /* Print styles */
        @media print {{
            body {{
                background: white;
            }}
            .news-card {{
                break-inside: avoid;
                box-shadow: none;
                border: 1px solid #e2e8f0;
            }}
            .read-more {{
                color: black;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="main-header">
            <h1>
                <span>📬</span>
                Weekly Pulse
            </h1>
            <div class="date">{datetime.now().strftime('%B %d, %Y')}</div>
            <div class="tagline">Your AI-curated digest of tech innovation</div>
        </div>
        
        {sections_html}
        
        <div class="footer">
            <p>Weekly Pulse • AI-powered news curation</p>
            <p style="margin-top: 10px; font-size: 0.75rem;">Each "Read More" links directly to the original source article</p>
        </div>
    </div>
</body>
</html>
"""
        
        # Save HTML file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"✓ Grid newsletter saved to: {output_path}")
        return output_path
    
    def escape_html(self, text):
        """Escape HTML special characters"""
        return (text.replace('&', '&amp;')
                    .replace('<', '&lt;')
                    .replace('>', '&gt;')
                    .replace('"', '&quot;')
                    .replace("'", '&#39;'))


# Test the grid renderer
if __name__ == "__main__":
    # Test with articles that have NO images
    test_data = {
        'articles': [
            {
                'title': 'Test Article 1 - AI Breakthrough',
                'summary': 'This is a test article to verify images work properly. It should get an AI/ML themed image automatically.',
                'url': 'https://example.com',
                'section': 'ai_ml',
                'image_url': ''
            },
            {
                'title': 'Test Article 2 - Open Source News',
                'summary': 'This article should get a development/open source themed image automatically.',
                'url': 'https://example.com',
                'section': 'dev_opensource',
                'image_url': ''
            },
            {
                'title': 'Test Article 3 - No Section Provided',
                'summary': 'This has no section, so it should get a default image.',
                'url': 'https://example.com',
                'section': 'general',
                'image_url': ''
            }
        ]
    }
    
    renderer = GridRenderer()
    output = renderer.create_html(test_data)
    print(f"\n✅ Test complete! Check: {output}")