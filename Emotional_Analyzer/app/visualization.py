import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os

def plot_sentiment_distribution(sentiment_counts, output_dir="outputs"):
    """Generate bar chart of sentiment distribution"""
    try:
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        plt.figure(figsize=(10, 6))
        
        # Define colors for sentiments
        colors = {'positive': '#2ecc71', 'neutral': '#3498db', 'negative': '#e74c3c'}
        sentiment_colors = [colors.get(sentiment, '#95a5a6') for sentiment in sentiment_counts.index]
        
        bars = plt.bar(sentiment_counts.index, sentiment_counts.values, color=sentiment_colors)
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'{int(height)}', ha='center', va='bottom')
        
        plt.title('Sentiment Distribution', fontsize=16, fontweight='bold')
        plt.ylabel('Count', fontsize=12)
        plt.xlabel('Sentiment', fontsize=12)
        plt.xticks(rotation=0)
        plt.grid(axis='y', alpha=0.3)
        plt.tight_layout()
        
        output_path = os.path.join(output_dir, 'sentiment_distribution.png')
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"📊 Sentiment distribution chart saved to {output_path}")
        return output_path
        
    except Exception as e:
        print(f"Error creating sentiment distribution plot: {e}")
        return None

def generate_wordcloud(text, output_dir="outputs"):
    """Create word cloud from text"""
    try:
        if not text or not text.strip():
            print("No text available for word cloud generation")
            return None
            
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        wordcloud = WordCloud(
            width=1200, 
            height=600, 
            background_color='white',
            max_words=100,
            colormap='viridis',
            relative_scaling=0.5,
            min_font_size=10
        ).generate(text)
        
        plt.figure(figsize=(15, 8))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title('Word Cloud - Most Common Words', fontsize=16, fontweight='bold', pad=20)
        plt.tight_layout(pad=0)
        
        output_path = os.path.join(output_dir, 'wordcloud.png')
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"☁️ Word cloud saved to {output_path}")
        return output_path
        
    except Exception as e:
        print(f"Error creating word cloud: {e}")
        return None

def plot_polarity_distribution(polarities, output_dir="outputs"):
    """Create histogram of polarity scores"""
    try:
        os.makedirs(output_dir, exist_ok=True)
        
        plt.figure(figsize=(12, 6))
        plt.hist(polarities, bins=30, alpha=0.7, color='skyblue', edgecolor='black')
        plt.axvline(x=0, color='red', linestyle='--', alpha=0.7, label='Neutral (0)')
        plt.title('Distribution of Polarity Scores', fontsize=16, fontweight='bold')
        plt.xlabel('Polarity Score', fontsize=12)
        plt.ylabel('Frequency', fontsize=12)
        plt.legend()
        plt.grid(alpha=0.3)
        plt.tight_layout()
        
        output_path = os.path.join(output_dir, 'polarity_distribution.png')
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"📈 Polarity distribution chart saved to {output_path}")
        return output_path
        
    except Exception as e:
        print(f"Error creating polarity distribution plot: {e}")
        return None