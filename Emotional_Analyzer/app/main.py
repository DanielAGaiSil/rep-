from analyzer import SentimentAnalyzer
from visualization import plot_polarity_distribution, generate_wordcloud, plot_sentiment_distribution
import pandas as pd
import os

def print_header():
    # Prints the CLI header

    print("=" * 50)
    print("Sentiment Analysis Tool")
    print("=" * 50)

def analyze_single_text(analyzer):
    # Handles single line input

    text = input("\nEnter text to analyze: ").strip()
    if not text :
        print(" Please input some text to analyze.")
        return
    
    result = analyzer.analyze_sentiment(text)

    print("\n" + "=" * 40)
    print("Analysis Results")
    print("=" * 40)
    print(f"Original text: {result["text"]}")
    print(f"Cleaned text: {result["cleaned_text"]}")
    print(f"Sentiment: {result["sentiment"].upper()} ({result["confidence"]} confidence)")
    print(f"Polarity: {result["polarity"]:.4f} (Range: -1 to 1)")
    print(f"Subjectivity: {result["subjectivity"]:.4f} (0 = objective, 1 = subjective)")

    # Interpretation

    if result["sentiment"] == "positive":
        print(" This text expresses a positive sentiment!")
    elif result["sentiment"] == "negative":
        print(" This text expresses a negative sentiment")
    else:
        print(" This text is neutral.")

def analyze_csv_file(analyzer):
    # Handling CSV file analysis

    file_path = input("\n Enter the path to the CSV file: ").strip()

    if not os.path.exists(file_path):
        print(f" File not found in: {file_path}")
        return
    
    try:
        # Reading the CSV file

        df = pd.read_csv(file_path)
        print(f" Loaded {len(df)} rows from {file_path}")

        # Checks for text column(s)
        
        text_columns = [col for col in df.columns if "text" in col.lower() or "comment" in col.lower() or "review" in col.lower()]
        
        if not text_columns:
            print("Available columns: ", list(df.columns))
            col_name = input("Enter the name of the column containing text: ").strip()
            if col_name not in df.columns:
                print(f" Column '{col_name}' not found.")
                return
            else:
                col_name = text_columns[0]
                print(f"Using column: '{col_name}'")
            
            # Clean data - remove NaN values

            df = df.dropna(subset = [col_name])
            texts = df[col_name].astype(str).tolist()

            print(f" Analyzing {len(texts)} texts.")

            # Analyze sentiments

            results = analyzer.analyze_batch(texts)
            results_df = pd.DataFrame(results)

            # Save results

            output_path = file_path.replace(".csv", "_sentiment_results.csv")
            results_df.to_csv(output_path, index = False)
            print(f" Results saved to {output_path}")

            # Print summary statistics
            print("=" * 40)
            print("📈Summary Statistics")
            print("=" * 40)
            sentiment_counts = results_df["sentiment"].value_counts()

            for sentiment, count in sentiment_counts.items():
                percentage = (count / len(results_df)) * 100
                print(f"{sentiment.capitalize()}: {count} ({percentage:.1f}%)")
            
            print(f"\nAverage Polarity: {results_df["polarity"].mean():.4f}")
            print(f"Average Subjectivity: {results_df['subjectivity'].mean():.4f}")

            # Generate visualizations
            print("\nGenerating visualizations.")
            plot_sentiment_distribution(sentiment_counts)

            # Creates word cloud from cleaned text
            all_text = " ".join([text for text in results_df["cleaned_text"] if text])
            if all_text.strip():
                generate_wordcloud(all_text)
            
            # Plot polarity distribution
            plot_polarity_distribution(results_df["polarity"].tolist())

            print("All visualizations saved to 'outputs' folder")


    except pd.errors.EmptyDataError:
        print("The CSV file is empty.")
    except pd.errors.ParserError:
        print("Error parsing CSV file. Please check file format.")
    except Exception as e:
        print(f"Error processing file: {str(e)}")

def main():
    # Main app loop
    print_header()

    # Initialize analyzer
    try:
        analyzer = SentimentAnalyzer()
    except Exception as e:
        print(f"Error initializing sentiment analyzer: {e}")
        return

    while True:
        print("\n" + "-"*30)
        print("MENU OPTIONS")
        print("-"*30)
        print("1. 📝 Analyze single text")
        print("2. 📊 Analyze CSV file")
        print("3. 🔴 Exit")

        try:
            choice = input("\nChoose option (1-3): ").strip()

            if choice == "1":
                analyze_single_text(analyzer)
            elif choice == "2":
                analyze_csv_file(analyzer)
            elif choice == "3":
                print("\nThank you for using my sentiment analyzer!")
                break
            else:
                print("Invalid option, please choose 1, 2 or 3.")

        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"An error occured: {e}")

if __name__ == "__main__":
    main()