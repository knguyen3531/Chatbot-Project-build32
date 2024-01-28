# main.py

# Importing modules from the chatbot package
from nlp_utils.preprocessing import preprocess
from nlp_utils.vectorization import vectorize_text
from seq2seq.translator import seq2seq_translate
from pattern_matching.matcher import pattern_match
from text_generation.generator import generate_text
from eliza import eliza_respond  # Importing the ELIZA module

def main():
    print("Hello! I'm your chatbot. (Type 'quit' to exit)")

    while True:
        # Get user input
        user_input = input("> ")

        # Check if the user wants to quit
        if user_input.lower() == "quit":
            break

        # ELIZA response
        eliza_response = eliza_respond(user_input)
        print("ELIZA: " + eliza_response)

        # Process the input (tokenization, stemming, lemmatization)
        stemmed_tokens, lemmatized_tokens = preprocess(user_input)
        print("Stemmed Tokens:", stemmed_tokens)
        print("Lemmatized Tokens:", lemmatized_tokens)

        # Vectorize the input text (bag-of-words)
        vectorized_text = vectorize_text(user_input)
        print("Vectorized Text:", vectorized_text.toarray())

        # Example of pattern matching (modify as needed)
        pattern = r'\b\w+\b'  # Simple pattern to match words
        matched_patterns = pattern_match(user_input, pattern)
        print("Matched Patterns:", matched_patterns)

        # Example of using the text generator (modify as needed)
        response_template = "You said: {text}"
        response = generate_text(response_template, {'text': user_input})
        print("Generated Response:", response)

        # Example of using the seq2seq translator (modify as needed)
        # translated_text = seq2seq_translate(user_input)
        # print("Translated Text:", translated_text)

# Entry point of the script
if __name__ == "__main__":
    main()
