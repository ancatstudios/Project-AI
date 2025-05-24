from transformers import pipeline

chatbot = pipeline("conversational", model="facebook/blenderbot-400M-distill")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Chatbot: Goodbye!")
        break
    response = chatbot(user_input)
    print("Chatbot:", response)

