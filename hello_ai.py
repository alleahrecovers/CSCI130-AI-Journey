
# hello_ai.py
# Name: Alleah MacSteves
# Date: October 26, 2026
# CSCI 130 - Introduction to Artificial Intelligence

from datetime import datetime

# Observe the environment: current time
current_hour = datetime.now().hour

if current_hour < 12:
    time_of_day = "morning"
elif current_hour < 17:
    time_of_day = "afternoon"
else:
    time_of_day = "evening"

print("Hello! Welcome to my first AI program.")
print(f"It is currently {time_of_day}.")

# Observe the user
mood = input("How are you feeling today? ").lower()

# Respond using fixed rules
if "happy" in mood or "good" in mood:
    print("That is great! Keep up the positive energy!")
elif "sad" in mood or "down" in mood:
    print("I'm sorry you're feeling that way. I hope things get better.")
elif "tired" in mood or "sleepy" in mood:
    print("Remember to take breaks and get some rest.")
elif "stressed" in mood or "overwhelmed" in mood:
    print("Take a deep breath and focus on one thing at a time.")
elif "excited" in mood:
    print("That's wonderful! I hope you have a great day!")
else:
    print("Thank you for sharing how you feel.")

# AI facts
print("\nHere are some AI facts:")
print("1. AI can recognize patterns in data.")
print("2. AI can help people translate languages.")
print("3. AI can help doctors analyze medical images.")
print("4. Some AI systems can generate text and images.")
