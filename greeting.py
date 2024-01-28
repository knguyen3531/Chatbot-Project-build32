# greeting.py

import re

# Regular expression pattern to match various greetings
pattern = r"[^a-z]*([y]o|[h']?ello|ok|hey|(good[ ])?(morn[gin']{0,3}|"\
          r"afternoon|even[gin']{0,3}))[\s,;:]{1,3}([a-z]{1,20})"
re_greeting = re.compile(pattern, flags=re.IGNORECASE)

# Sets of names
my_names = set(['rosa', 'rose', 'chatty', 'chatbot', 'bot', 'chatterbot'])
curt_names = set(['hal', 'you', 'u'])
greeter_name = ''  # You might want to initialize this with a specific name

def generate_greeting(user_input):
    match = re_greeting.match(user_input)
    response = "That doesn't seem like a greeting I recognize."

    if match:
        at_name = match.groups()[-1]

        if at_name in curt_names:
            response = "Good one."
        elif at_name.lower() in my_names:
            response = "Hi {}, How are you?".format(greeter_name)
        else:
            response = "Hello there!"  # A general response for names not in the lists

    return response
