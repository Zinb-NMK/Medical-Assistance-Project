import json
import random

def load_intents(path='intents.json'):
    with open(path) as file:
        data = json.load(file)
    return data

def chatbot_response(user_input):
    intents = load_intents()
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            if pattern.lower() in user_input.lower():
                return random.choice(intent['responses'])
    return "I'm not sure about that. Can you elaborate?"