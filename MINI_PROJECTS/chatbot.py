import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

print("Chatbot: Hello! Type 'exit' to end the conversation.")

while True:
    user_input = input("You: ")

    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break

    # Process the user's message with spaCy
    doc = nlp(user_input)

    # Basic response handling
    if "how are you" in user_input.lower():
        print("Chatbot: I'm just a computer program, but I'm doing well. How can I assist you today?")
    elif "your name" in user_input.lower():
        print("Chatbot: I'm a chatbot. You can call me ChatGPT.")
    else:
        print("Chatbot: I'm not sure how to respond to that. Can you ask me something else?")