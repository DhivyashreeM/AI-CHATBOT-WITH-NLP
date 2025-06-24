import nltk
import spacy
from nltk.chat.util import Chat, reflections
import random
from datetime import datetime

nltk.download('punkt')
nltk.download('wordnet')

try:
    nlp = spacy.load('en_core_web_sm')
except:
    print("spaCy English model not found. Installing...")
    import subprocess
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load('en_core_web_sm')

pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you today?", "Hi there! What can I do for you?", "Hey! What's on your mind?"]
    ],
    [
        r"what is your name?",
        ["I'm ChatBot, your virtual assistant.", "You can call me ChatBot.", "I go by the name ChatBot."]
    ],
    [
        r"how are you?",
        ["I'm doing well, thanks for asking!", "I'm just a bot, but I'm functioning perfectly!", "All systems go!"]
    ],
    [
        r"(.*) your name (.*)",
        ["I'm ChatBot!", "The name's ChatBot. Virtual assistant at your service!"]
    ],
    [
        r"what can you do|help",
        ["I can answer questions, tell you the time, discuss various topics, and more! What do you need?"]
    ],
    [
        r"time|what time is it",
        [f"The current time is {datetime.now().strftime('%H:%M')}"]
    ],
    [
        r"date|today's date",
        [f"Today's date is {datetime.now().strftime('%Y-%m-%d')}"]
    ],
    [
        r"quit|bye|goodbye",
        ["Goodbye! Have a great day!", "It was nice chatting with you!", "See you later!"]
    ],
    [
        r"(.*) (weather|temperature) (.*)",
        ["I'm not connected to weather services, but you can check your favorite weather app!"]
    ],
    [
        r"(.*) (age|old) (.*)",
        ["I'm just a program, so I don't have an age!", "Age is just a number for a chatbot like me!"]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Could you rephrase that?",  
         "I'm still learning. Can you ask me something else?"]
    ]
]

class EnhancedChatBot:
    def __init__(self):
        self.chatbot = Chat(pairs, reflections)
        self.context = {}
        
    def preprocess_text(self, text):
        doc = nlp(text.lower())
        processed = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
        return ' '.join(processed)
    
    def respond(self, user_input):
        response = self.chatbot.respond(user_input)

        if not response:
            processed_input = self.preprocess_text(user_input)
            response = self.chatbot.respond(processed_input)
            
        if not response:
            response = random.choice(pairs[-1][1])
            
        return response
    
    def start_chat(self):
        print("ChatBot: Hello! I'm your virtual assistant. Type 'quit' to exit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['quit', 'bye', 'goodbye', 'exit']:
                print("ChatBot: Goodbye! Have a great day!")
                break
            response = self.respond(user_input)
            print(f"ChatBot: {response}")

if __name__ == "__main__":
    bot = EnhancedChatBot()
    bot.start_chat()
