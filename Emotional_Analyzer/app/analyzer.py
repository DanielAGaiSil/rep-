from textblob import TextBlob
from utils import clean_text, download_nltk_data

class SentimentAnalyzer:
    def __init__(self):
        """Initialize the sentiment analyzer and download required data"""
        download_nltk_data()

    def analyze_sentiment(self, text):
        """
        Analyze sentiment of given text
        
        Args:
            text (str): Text to analyze
            
        Returns:
            dict: Dictionary containing analysis results
        """
        if not text or not isinstance(text, str):
            return {
                'text': text,
                'cleaned_text': '',
                'polarity': 0.0,
                'subjectivity': 0.0,
                'sentiment': 'neutral',
                'confidence': 'low'
            }
        
        try:
            cleaned = clean_text(text)
            blob = TextBlob(cleaned if cleaned else text)
            
            polarity = blob.sentiment.polarity
            subjectivity = blob.sentiment.subjectivity
            
            # Determine sentiment with confidence levels
            if polarity > 0.1:
                sentiment = 'positive'
                confidence = 'high' if polarity > 0.5 else 'medium'
            elif polarity < -0.1:
                sentiment = 'negative'
                confidence = 'high' if polarity < -0.5 else 'medium'
            else:
                sentiment = 'neutral'
                confidence = 'low'
            
            return {
                'text': text,
                'cleaned_text': cleaned,
                'polarity': round(polarity, 4),
                'subjectivity': round(subjectivity, 4),
                'sentiment': sentiment,
                'confidence': confidence
            }
            
        except Exception as e:
            print(f"Error analyzing sentiment: {e}")
            return {
                'text': text,
                'cleaned_text': '',
                'polarity': 0.0,
                'subjectivity': 0.0,
                'sentiment': 'neutral',
                'confidence': 'error'
            }

    def analyze_batch(self, texts):
        """
        Analyze sentiment for a list of texts
        
        Args:
            texts (list): List of texts to analyze
            
        Returns:
            list: List of analysis results
        """
        results = []
        for i, text in enumerate(texts):
            if i % 100 == 0 and i > 0:
                print(f"Processed {i} texts...")
            results.append(self.analyze_sentiment(text))
        return results