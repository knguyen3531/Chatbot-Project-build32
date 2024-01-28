# vectorization.py

# Import CountVectorizer for text vectorization
from sklearn.feature_extraction.text import CountVectorizer

def vectorize_text(text):
    """
    Function to vectorize text using the Bag-of-Words model.
    """
    # Initialize the CountVectorizer
    vectorizer = CountVectorizer()

    # Fit and transform the text to a vector
    vectorized_text = vectorizer.fit_transform([text])
    return vectorized_text
