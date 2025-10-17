import datetime
import random

def greet_user():
    name = input("Enter your name: ")
    greetings = ["Hello", "Hi", "Welcome", "Hey", "Greetings"]
    greeting = random.choice(greetings)
    now = datetime.datetime.now()
    print(f"{greeting}, {name}! The current time is {now:%H:%M:%S}.")

if __name__ == "__main__":
    greet_user()

