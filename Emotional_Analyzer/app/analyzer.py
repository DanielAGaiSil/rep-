from textblob import TextBlob
from utils import clean_text, download_nltk_data

class SentimentAnalyzer:
    def __init__(self):
        # Initialize the sentiment analyzer and download the required data

        download_nltk_data()

    def analyze_sentiment(self, text):
        # Analyze sentiment of any given text
        # Arguments: text (str): Text to analyze
        # Then returns: dict: dictionary containing analysis results
        if not text or not isinstance(text, str):
            return {
                "text": text,
                "cleaned_text": "",
                "polarity": 0.0,
                "subjectivity": 0.0,
                "sentiment": 0.0,
                "confidence": "low"
            }
        try:
            # This calls clean_text in order to standardize text
            # Eg: clean_text("I LOVE this product! It's AMAZING!") returns: "love product amazing"
            # Making it easier to analyze
            cleaned = clean_text(text)
            blob = TextBlob(cleaned if cleaned else text)
            # Blob is so to make sure it's not an empty string of text to analyze
            # And "else text" is to use the original text in case of empty cleaned oh and also non-english text

            polarity = blob.sentiment.polarity
            subjectivity = blob.sentiment.subjectivity

            # Determines sentimnents depending on confidence level

            if polarity > 0.1:
                sentiment = "positive"
                confidence = "high" if polarity > 0.5 else "medium"
            elif polarity < -0.1:
                sentiment = "negative"
                confidence = "high" if polarity < -0.5 else "medium"
            else:
                sentiment = "neutral"
                confidence = "low"
            
            return {
                "text": text,
                "cleaned_text": cleaned,
                "polarity": round(polarity, 4),
                "subjectivity": round(subjectivity, 4),
                "sentiment": sentiment,
                "confidence": confidence
            }
        
        except Exception as e:
            print(f"Error  analyzing content: {e}")
            return {
                "text": text,
                "cleaned_text": '',
                "polarity": 0.0,
                "subjectivity": 0.0,
                "sentiment": 'neutral',
                "confidence": 'error'
            }
        
    def analyze_batch(self, texts):
        # Analyzes sentiment for a list of texts
        # Arguments: texts(list): List of texts to analyze
        # Returning: list: List of analysis results
        results = []
        for i, text in enumerate(texts):
            if i % 100 == 0 and i > 0:
                print(f"Processed {i} texts.")
                results.append(self.analyze_sentiment(text))
        return results