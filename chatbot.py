def general_chatbot():
    print("🤖 Hello! I'm your chatbot. Ask me anything.")
    print("Type 'exit' to end the chat.\n")

    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm just a program, but I'm functioning well! 😄",
        "what is your name": "I'm a simple Python chatbot created to chat with you.",
        "help": "You can ask me general questions or type 'exit' to leave.",
        "bye": "Goodbye! Have a great day!",
        "thank you": "You're welcome!",
        "time": "Sorry, I can't tell time yet, but you can check your device clock!",
    }

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "exit":
            print("Bot: Chat ended. 👋")
            break

        matched = False
        for keyword in responses:
            if keyword in user_input:
                print("Bot:", responses[keyword])
                matched = True
                break

        if not matched:
            print("Bot: I don't understand that. Try asking something else or type 'help'.")

# Run the chatbot
if __name__ == "__main__":
    general_chatbot()
