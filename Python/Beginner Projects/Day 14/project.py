from art import logo, vs
from game_data import data
import random
from replit import clear

guesses = 0
final_score = 0
game_on = True

while game_on:
    if guesses == 0:
        choice_a = random.choice(data)
    choice_b = random.choice(data)
    if choice_a == choice_b:
        choice_b = random.choice(data)
    
    clear() 
    print(logo)
    if guesses > 0:
        print(f"You're right! Current score: {guesses}")
    elif guesses == -1:
        print(f"Sorry, that's wrong. Final score: {final_score}")
        break
    print(f"Compare A: {choice_a['name']}, {choice_a['description']} from {choice_a['country']}.")
    print(vs)
    print(f"Against B: {choice_b['name']}, {choice_b['description']} from {choice_b['country']}.")
    
    while True:
        user_choice = input("Who has more followers? Type 'A' or 'B': ")

        if user_choice == 'A':
            if choice_a['follower_count'] > choice_b['follower_count']:
                guesses += 1
                choice_a = choice_b
            else:
                final_score = guesses
                guesses = -1
            break
        elif user_choice == 'B':
            if choice_b['follower_count'] > choice_a['follower_count']:
                guesses += 1
                choice_a = choice_b
            else:
                final_score = guesses
                guesses = -1
            break
        else:
            print("Please try again")
    
