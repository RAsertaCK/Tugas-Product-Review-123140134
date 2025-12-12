from transformers import pipeline

class SentimentAnalyzer:
    def __init__(self):
        self.classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

    def analyze(self, text: str) -> str:
        """Menganalisis sentimen dan mengembalikan 'Positive', 'Negative', atau 'Neutral'."""
        if not text:
            return "Neutral"
        try:
            result = self.classifier(text)[0]
            label = result['label']
            score = result['score']
            
            if label == 'POSITIVE':
                return "Positive"
            elif label == 'NEGATIVE':
                return "Negative"
            else:
                return "Neutral"
        except Exception as e:
            print(f"Error during sentiment analysis: {e}")
            return "Neutral"