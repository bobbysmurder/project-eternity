# eternity_ai.py
import os
import time
import random
import re
import sys

# This is the AI code — it's like a digital brain that can talk, think, and learn.
# You can add more features, like making it talk in different languages or do math.

def think(question):
    # This is where the AI "thinks" — it's like a digital brain processing your question.
    print("Thinking... 🧠")
    time.sleep(1)  # Let's pretend it's thinking for a second.
    return "I think the answer is: " + question

def talk():
    # This is where the AI "talks" — it's like a digital voice that can chat with you.
    print("Hello, I'm Dig — your AI assistant! 🌟")
    while True:
        user_input = input("Ask me anything: ")
        if user_input.lower() in ["exit", "quit", "goodbye"]:
            print("Goodbye! 🌟")
            break
        print(think(user_input))

if __name__ == "__main__":
    talk()
