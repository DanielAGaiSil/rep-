import re
import nltk
from nltk.corpus import stopwords
import sys

def download_nltk_data():
    """Download required NLTK data with error handling"""
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        print("Downloading NLTK punkt tokenizer...")
        nltk.download('punkt', quiet=True)
    
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        print("Downloading NLTK stopwords...")
        nltk.download('stopwords', quiet=True)

def clean_text(text):
    """Preprocess text for analysis"""
    if not isinstance(text, str):
        return ""
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation but keep spaces
    text = re.sub(r'[^\w\s]', '', text)
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    try:
        # Tokenize
        words = nltk.word_tokenize(text)
        
        # Remove stopwords and short words
        stop_words = set(stopwords.words('english'))
        words = [word for word in words if word not in stop_words and len(word) > 2]
        
        return " ".join(words)
    except Exception as e:
        print(f"Error in text cleaning: {e}")
        return text