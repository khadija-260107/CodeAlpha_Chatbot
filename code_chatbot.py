# =============================================
# TASK 4: RULE-BASED CHATBOT
# CodeAlpha Internship — Python Programming
# =============================================

import datetime
import random

# All responses stored in a dictionary — easy to expand
responses = {
    # Greetings
    "hello":         "Hello! How can I assist you today?",
    "hi":            "Hi there! What can I do for you?",
    "hey":           "Hey! How can I help?",
    "good morning":  "Good morning! Hope you have a productive day.",
    "good afternoon":"Good afternoon! How can I help?",
    "good evening":  "Good evening! What can I do for you?",

    # About the bot
    "what is your name":     "My name is CodeBot, a rule-based assistant.",
    "who are you":           "I am CodeBot, built as part of a Python internship project.",
    "what can you do":       "I can answer basic questions, tell jokes, give the time and date, and have a simple conversation.",
    "are you a robot":       "Yes, I am a program — not a human.",
    "are you human":         "No, I am a chatbot built with Python.",

    # Time and date
    "what time is it":       None,   # handled separately
    "what is the date":      None,   # handled separately
    "what day is it":        None,   # handled separately

    # Weather (static response since no API)
    "how is the weather":    "I don't have access to live weather data. Please check weather.com for updates.",
    "what is the weather":   "I don't have real-time weather access. Try a weather app for accurate info.",

    # Feelings
    "how are you":           "I am functioning as expected. How about you?",
    "how are you doing":     "Running smoothly, thank you for asking.",
    "are you okay":          "Yes, all systems are working fine.",

    # General knowledge
    "what is python":        "Python is a high-level, general-purpose programming language known for its simplicity and readability.",
    "what is programming":   "Programming is the process of writing instructions that a computer can execute to perform specific tasks.",
    "what is ai":            "Artificial Intelligence is the simulation of human intelligence in machines that can learn, reason, and solve problems.",
    "what is machine learning": "Machine Learning is a branch of AI where systems learn from data to improve their performance over time.",

    # Jokes
    "tell me a joke":        None,   # handled separately
    "joke":                  None,

    # Help
    "help":                  "You can ask me about: time, date, jokes, Python, AI, greetings, or general questions.",

    # Exit
    "bye":       "Goodbye! Have a great day.",
    "goodbye":   "Goodbye! Take care.",
    "exit":      "Exiting the chat. Goodbye.",
    "quit":      "Exiting the chat. Goodbye."
}

# A list of jokes for variety
jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "Why was the developer broke? Because he used up all his cache.",
    "How do you comfort a JavaScript developer? You console them.",
    "A SQL query walks into a bar, walks up to two tables and asks: Can I join you?",
    "Why do Python programmers wear glasses? Because they cannot C.",
    "What is a computer's favorite snack? Microchips."
]

def get_time_response(user_input):
    now = datetime.datetime.now()
    if "time" in user_input:
        return f"The current time is {now.strftime('%I:%M %p')}."
    elif "date" in user_input:
        return f"Today's date is {now.strftime('%B %d, %Y')}."
    elif "day" in user_input:
        return f"Today is {now.strftime('%A')}."
    return None

def get_response(user_input):
    user_input = user_input.lower().strip()

    # Check for exit commands
    if user_input in ["bye", "goodbye", "exit", "quit"]:
        return responses[user_input], True   # True means exit

    # Check for time/date/day
    time_response = get_time_response(user_input)
    if time_response:
        return time_response, False

    # Check for jokes
    if "joke" in user_input:
        return random.choice(jokes), False

    # Check exact match in responses dictionary
    if user_input in responses:
        return responses[user_input], False

    # Check partial match — useful for longer sentences
    for key in responses:
        if key in user_input:
            return responses[key], False

    # Default fallback
    return "I am not sure how to respond to that. Type 'help' to see what I can do.", False


def main():
    print("=" * 50)
    print("         CODEBOT - RULE BASED CHATBOT")
    print("         Built with Python")
    print("=" * 50)
    print("Type 'help' to see available commands.")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            print("CodeBot: Please type something.\n")
            continue

        reply, should_exit = get_response(user_input)
        print(f"CodeBot: {reply}\n")

        if should_exit:
            break

main()