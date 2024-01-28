# preprocessing.py

# Import necessary libraries for NLP tasks
import nltk
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.tokenize import word_tokenize

# Download required datasets
nltk.download('punkt')
nltk.download('wordnet')

def preprocess(text):
    """
    Function to preprocess text by tokenization, stemming, and lemmatization.
    """
    # Tokenization
    tokens = word_tokenize(text)

    # Stemming
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]

    return stemmed_tokens, lemmatized_tokens
