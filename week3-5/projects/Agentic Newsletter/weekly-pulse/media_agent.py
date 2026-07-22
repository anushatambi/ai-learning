"""
Media Agent - Fetches and manages images for newsletter sections
"""
import requests
from datetime import datetime
import random

class MediaAgent:
    """Fetches relevant images for newsletter sections"""
    
    def __init__(self):
        print("Media Agent initialized")
        self.image_cache = {}
        self.used_images = set()  # Track used images to prevent duplicates
        
        # Detailed image mapping for each section type with multiple options
        self.category_images = {
            'ai_ml': [
                {'url': 'https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=600&h=300&fit=crop', 'alt': 'AI and Machine Learning visualization'},
                {'url': 'https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&h=300&fit=crop', 'alt': 'Artificial Intelligence brain concept'},
                {'url': 'https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=600&h=300&fit=crop', 'alt': 'Neural network AI concept'}
            ],
            'dev_opensource': [
                {'url': 'https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?w=600&h=300&fit=crop', 'alt': 'Open source development code'},
                {'url': 'https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&h=300&fit=crop', 'alt': 'Developer writing code'},
                {'url': 'https://images.unsplash.com/photo-1461749280684-dccba630e2f6?w=600&h=300&fit=crop', 'alt': 'Coding on laptop'}
            ],
            'industry': [
                {'url': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&h=300&fit=crop', 'alt': 'Industry and business analytics'},
                {'url': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600&h=300&fit=crop', 'alt': 'Industry trends and business'},
                {'url': 'https://images.unsplash.com/photo-1551434678-e076c2236d9b?w=600&h=300&fit=crop', 'alt': 'Business growth metrics'}
            ],
            'hackathon': [
                {'url': 'https://images.unsplash.com/photo-1504384764586-bb4cdc1707b0?w=600&h=300&fit=crop', 'alt': 'Hackathon competition coding'},
                {'url': 'https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?w=600&h=300&fit=crop', 'alt': 'Hackathon team working'},
                {'url': 'https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&h=300&fit=crop', 'alt': 'Team collaboration event'}
            ],
            'datascience': [
                {'url': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&h=300&fit=crop', 'alt': 'Data science visualization'},
                {'url': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&h=300&fit=crop', 'alt': 'Data analytics dashboard'},
                {'url': 'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&h=300&fit=crop', 'alt': 'Big data processing'}
            ],
            'general': [
                {'url': 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&h=300&fit=crop', 'alt': 'Technology and innovation'},
                {'url': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&h=300&fit=crop', 'alt': 'Tech innovation concept'}
            ]
        }
    
    def fetch_image_for_section(self, section):
        """Fetch relevant image for a newsletter section with NO duplicates"""
        category = section.get('category', 'general')
        
        # Try to match category (handle variations)
        matched_category = None
        for key in self.category_images.keys():
            if category in key or key in category:
                matched_category = key
                break
        
        if not matched_category:
            matched_category = 'general'
        
        # Get available images for this category
        available_images = self.category_images[matched_category][:]
        
        # Filter out already used images
        unused_images = [img for img in available_images if img['url'] not in self.used_images]
        
        # If all images are used, reset the used_images for this category
        if not unused_images:
            print(f"  ⚠ All images used for {matched_category}, resetting cache")
            # Clear used images for this category only
            for img in available_images:
                if img['url'] in self.used_images:
                    self.used_images.remove(img['url'])
            unused_images = available_images
        
        # Pick first available image
        image_data = unused_images[0]
        
        # Mark as used
        self.used_images.add(image_data['url'])
        
        return {
            'url': image_data['url'],
            'attribution': '📷 Unsplash',
            'alt_text': image_data['alt']
        }
    
    def add_images_to_newsletter(self, newsletter):
        """Add images to each section in the newsletter"""
        print("Adding images to newsletter sections...")
        
        sections_with_images = []
        
        for idx, section in enumerate(newsletter.get('sections', [])):
            # Fetch image for this section
            image_data = self.fetch_image_for_section(section)
            
            # Create enriched section with image
            enriched_section = section.copy()
            enriched_section['image'] = image_data
            
            sections_with_images.append(enriched_section)
            print(f"  ✓ Added {image_data['alt_text']} to: {section.get('header', 'Unknown')}")
        
        # Update newsletter with images
        newsletter['sections'] = sections_with_images
        newsletter['has_images'] = True
        
        print(f"✓ Added images to {len(sections_with_images)} sections (all unique)")
        return newsletter

# Test the media agent
if __name__ == "__main__":
    test_newsletter = {
        'sections': [
            {'header': 'AI Breakthroughs', 'category': 'ai_ml', 'intro': 'Test', 'bullets': ['Test']},
            {'header': 'Open Source News', 'category': 'dev_opensource', 'intro': 'Test', 'bullets': ['Test']},
            {'header': 'Industry News', 'category': 'industry', 'intro': 'Test', 'bullets': ['Test']}
        ]
    }
    
    media = MediaAgent()
    enhanced = media.add_images_to_newsletter(test_newsletter)
    
    for section in enhanced['sections']:
        print(f"\n{section['header']}: {section['image']['alt_text']}")