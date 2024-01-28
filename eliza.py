# eliza.py

import re
import random

# ELIZA's reflection mechanism
reflections = {
    "am": "are",
    "was": "were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "are": "am",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

# ELIZA's response patterns
psychobabble = [
    (r'I need (.*)',
     ("Why do you need {0}?",
      "Would it really help you to get {0}?",
      "Are you sure you need {0}?")),

    # Add more patterns here...

    # Default response if no patterns are matched
    (r'.*',
     ("Please tell me more.",
      "Let's change focus a bit... Tell me about your family.",
      "Can you elaborate on that?",
      "Why do you say that {0}?",
      "I see.",
      "Very interesting.",
      "How does that make you feel?",
      "How do you feel when you say that?"))
]

def reflect(fragment):
    tokens = fragment.lower().split()
    for i, token in enumerate(tokens):
        if token in reflections:
            tokens[i] = reflections[token]
    return ' '.join(tokens)

def eliza_respond(statement):
    for pattern, responses in psychobabble:
        match = re.match(pattern, statement.rstrip(".!"))
        if match:
            response = random.choice(responses)
            groups = match.groups()
            if groups:
                return response.format(*[reflect(g) for g in groups])
            else:
                return response.format(statement)
    return "I'm not sure I understand you fully."
