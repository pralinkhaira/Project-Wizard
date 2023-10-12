import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'How can I help you today?']),
    (r'what is your name?', ["I'm a chatbot.", "I don't have a name."]),
    (r'how are you|how are you doing', ["I'm just a program, but I'm functioning properly."]),
    (r'quit|exit', ['Goodbye!', 'Bye!', 'Take care!']),
]

# Define reflections to transform first-person pronouns to second-person and vice versa
reflections = {
    "i": "you",
    "i am": "you are",
    "my": "your",
    "you": "I",
    "me": "you",
}

# Create a chatbot instance
chatbot = Chat(patterns, reflections)

# Function to start the chat
def chat():
    print("Chatbot: Hello! How can I assist you today? Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    nltk.download('punkt')  # Download necessary NLTK data (if not already downloaded)
    chat()
    