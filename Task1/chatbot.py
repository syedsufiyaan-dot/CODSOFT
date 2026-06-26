print("🤖 Welcome to the Rule-Based Chatbot!")
print("Type 'bye' to end the conversation.\n")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi" or user == "hey":
        print("Bot: Hello! How can I help you today?")

    elif "how are you" in user:
        print("Bot: I'm doing great! Thanks for asking.")

    elif "your name" in user:
        print("Bot: My name is CodSoft ChatBot.")

    elif "who created you" in user:
        print("Bot: I was created using Python for the CodSoft AI Internship.")

    elif "help" in user:
        print("Bot: I can answer simple questions like greetings, time, date, and more.")

    elif "time" in user:
        from datetime import datetime
        current_time = datetime.now().strftime("%I:%M %p")
        print(f"Bot: Current time is {current_time}")

    elif "date" in user:
        from datetime import datetime
        current_date = datetime.now().strftime("%d-%m-%Y")
        print(f"Bot: Today's date is {current_date}")

    elif "thank you" in user or "thanks" in user:
        print("Bot: You're welcome!")

    elif user == "bye":
        print("Bot: Goodbye! Have a great day!")
        break

    else:
        print("Bot: Sorry, I don't understand that. Please ask something else.")
