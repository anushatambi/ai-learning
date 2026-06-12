import json

class LearningTracker:
    def __init__(self, current_week):
        self.topics_studied = []
        self.days_completed = 0
        self.current_week = current_week

    def mark_topic_complete(self, topic, increment_day=True):
        self.topics_studied.append(topic)
        if increment_day:
            self.days_completed += 1
        print(f"✅ '{topic}' marked complete! Days completed: {self.days_completed}")
    
    def calculate_completion(self, total_topics):
        percentage = (len(self.topics_studied) / total_topics) * 100
        return f"Progress: {len(self.topics_studied)}/{total_topics} topics — {percentage:.1f}% complete"

    def export_progress(self, filename):
        data = {
            "current_week": self.current_week,
            "days_completed": self.days_completed,
            "topics_studied": self.topics_studied,
            "total_topics_completed": len(self.topics_studied)
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
        print(f"Progress exported to {filename}")


tracker = LearningTracker(current_week=3)
tracker.mark_topic_complete("Variables & Types")
tracker.mark_topic_complete("Functions")
tracker.mark_topic_complete("Error Handling")
tracker.mark_topic_complete("APIs")
tracker.mark_topic_complete("OOP")

print(tracker.calculate_completion(total_topics=10))
tracker.export_progress("progress.json")