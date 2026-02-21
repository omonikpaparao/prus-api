import nltk
import textblob

def download_assets():
    try:
        # Downloads the specific corpora TextBlob requires
        nltk.download('punkt_tab') # Updated for latest NLTK/TextBlob versions
        nltk.download('brown')
        nltk.download('wordnet')
        nltk.download('averaged_perceptron_tagger_eng')
        print("NLTK/TextBlob data downloaded successfully.")
    except Exception as e:
        print(f"Error downloading data: {e}")

if __name__ == "__main__":
    download_assets()
