import unittest
import sys
import os

# Add the current directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.analyzer import SentimentAnalyzer

class TestSentimentAnalyzer(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Set up test fixtures before running tests"""
        print("Setting up SentimentAnalyzer for testing...")
        cls.analyzer = SentimentAnalyzer()
    
    def test_positive_sentiment(self):
        """Test positive sentiment detection"""
        positive_texts = [
            "I love this! It's amazing and wonderful.",
            "This is fantastic and great!",
            "Excellent work, I'm very happy with this."
        ]
        
        for text in positive_texts:
            with self.subTest(text=text):
                result = self.analyzer.analyze_sentiment(text)
                self.assertEqual(result['sentiment'], 'positive')
                self.assertGreater(result['polarity'], 0)
    
    def test_negative_sentiment(self):
        """Test negative sentiment detection"""
        negative_texts = [
            "I hate this! It's terrible and awful.",
            "This is horrible and disgusting!",
            "Worst experience ever, completely disappointed."
        ]
        
        for text in negative_texts:
            with self.subTest(text=text):
                result = self.analyzer.analyze_sentiment(text)
                self.assertEqual(result['sentiment'], 'negative')
                self.assertLess(result['polarity'], 0)
    
    def test_neutral_sentiment(self):
        """Test neutral sentiment detection"""
        neutral_texts = [
            "This is a pencil.",
            "The weather is cloudy today.",
            "I went to the store."
        ]
        
        for text in neutral_texts:
            with self.subTest(text=text):
                result = self.analyzer.analyze_sentiment(text)
                self.assertEqual(result['sentiment'], 'neutral')
                self.assertAlmostEqual(result['polarity'], 0, delta=0.15)
    
    def test_empty_text(self):
        """Test handling of empty text"""
        result = self.analyzer.analyze_sentiment("")
        self.assertEqual(result['sentiment'], 'neutral')
        self.assertEqual(result['polarity'], 0.0)
        self.assertEqual(result['confidence'], 'low')
    
    def test_none_text(self):
        """Test handling of None input"""
        result = self.analyzer.analyze_sentiment(None)
        self.assertEqual(result['sentiment'], 'neutral')
        self.assertEqual(result['polarity'], 0.0)
        self.assertEqual(result['confidence'], 'low')
    
    def test_non_string_input(self):
        """Test handling of non-string input"""
        result = self.analyzer.analyze_sentiment(123)
        self.assertEqual(result['sentiment'], 'neutral')
        self.assertEqual(result['polarity'], 0.0)
    
    def test_result_structure(self):
        """Test that results have the expected structure"""
        text = "This is a test sentence."
        result = self.analyzer.analyze_sentiment(text)
        
        # Check that all expected keys are present
        expected_keys = ['text', 'cleaned_text', 'polarity', 'subjectivity', 'sentiment', 'confidence']
        for key in expected_keys:
            self.assertIn(key, result)
        
        # Check data types
        self.assertIsInstance(result['text'], str)
        self.assertIsInstance(result['cleaned_text'], str)
        self.assertIsInstance(result['polarity'], (int, float))
        self.assertIsInstance(result['subjectivity'], (int, float))
        self.assertIsInstance(result['sentiment'], str)
        self.assertIsInstance(result['confidence'], str)
        
        # Check value ranges
        self.assertGreaterEqual(result['polarity'], -1)
        self.assertLessEqual(result['polarity'], 1)
        self.assertGreaterEqual(result['subjectivity'], 0)
        self.assertLessEqual(result['subjectivity'], 1)
        self.assertIn(result['sentiment'], ['positive', 'negative', 'neutral'])
        self.assertIn(result['confidence'], ['low', 'medium', 'high', 'error'])
    
    def test_batch_analysis(self):
        """Test batch analysis functionality"""
        texts = [
            "I love this product!",
            "This is terrible.",
            "It's okay, nothing special.",
            "Amazing experience!"
        ]
        
        results = self.analyzer.analyze_batch(texts)
        
        self.assertEqual(len(results), len(texts))
        
        expected_sentiments = ['positive', 'negative', 'neutral', 'positive']
        for i, result in enumerate(results):
            self.assertEqual(result['sentiment'], expected_sentiments[i])
    
    def test_confidence_levels(self):
        """Test confidence level assignment"""
        # High confidence positive
        result = self.analyzer.analyze_sentiment("This is absolutely amazing and wonderful!")
        self.assertEqual(result['sentiment'], 'positive')
        
        # High confidence negative  
        result = self.analyzer.analyze_sentiment("This is absolutely terrible and horrible!")
        self.assertEqual(result['sentiment'], 'negative')
        
        # Test that confidence is assigned
        self.assertIn(result['confidence'], ['low', 'medium', 'high'])

def run_tests():
    """Run all tests with detailed output"""
    print("Running Sentiment Analyzer Tests...")
    print("=" * 50)
    
    # Create test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSentimentAnalyzer)
    
    # Run tests with detailed output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "=" * 50)
    if result.wasSuccessful():
        print("✅ All tests passed!")
    else:
        print(f"❌ {len(result.failures)} test(s) failed, {len(result.errors)} error(s)")
    
    return result.wasSuccessful()

if __name__ == '__main__':
    run_tests()