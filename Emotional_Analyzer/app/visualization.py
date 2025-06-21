import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os

def plot_sentiment_distribution(sentiment_counts, output_dir = "ouputs"):
    # Generates a bar chart of sentiments distribution

    try:
        # Create the directory if it doesn't exist

        os.makedirs(output_dir, exist_ok = True)

        plt.figure(figsize = (10, 6))

        colors = {"positive": "#2ecc71", "neutral": "#3498db", "negative": "#e74c3c"}
        sentiment_colors = [colors.get(sentiment, "#95a5a6") for sentiment in sentiment_counts.index]

        bars = plt.bar(sentiment_counts.index, sentiment_counts.values, color = sentiment_colors)

        # Adds value labels to the bars

        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                     f"{int(height)}", ha = "center", va ="bottom")
        
        plt.title("Sentiment Distribution", fontsize = 16, fontheight = "bold")
        plt.ylabel("Count", fontsize = 12)
        plt.xlabel("Sentiment", fontsize = 12)
        plt.xticks()            