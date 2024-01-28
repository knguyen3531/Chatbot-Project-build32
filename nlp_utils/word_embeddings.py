# word_embeddings.py

# Import gensim library for word embeddings
import gensim.downloader as api

def get_word_vectors(text):
    """
    Function to get word vectors for each word in the text using a pre-trained model.
    """
    # Load a pre-trained word2vec model
    word2vec_model = api.load('word2vec-google-news-300')

    # Get word vectors for each word in the text
    word_vectors = [word2vec_model[word] for word in text if word in word2vec_model]
    return word_vectors
