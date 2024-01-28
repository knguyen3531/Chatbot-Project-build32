# matcher.py

# Import regular expression library
import re

def pattern_match(text, pattern):
    """
    Function to find patterns in text using regular expressions.
    """
    # Find all occurrences of the pattern in the text
    matches = re.findall(pattern, text)
    return matches
