# main.py

# Importing modules from the chatbot package
from nlp_utils.preprocessing import preprocess
from nlp_utils.vectorization import vectorize_text
from seq2seq.translator import seq2seq_translate
from pattern_matching.matcher import pattern_match
from text_generation.generator import generate_text

def main():
    # Get user input
    user_input = input("Enter your message: ")

    # Process the input (tokenization, stemming, lemmatization)
    processed_text = preprocess(user_input)

    # Vectorize the input text (bag-of-words)
    vectorized_text = vectorize_text(user_input)

    # Other functionalities can be added here as needed

# Entry point of the script
if __name__ == "__main__":
    main()
