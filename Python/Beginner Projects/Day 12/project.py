import random 

def check_score(a_num, a_guess):
    if a_num < a_guess:
        print("Too high.")
        return True
    elif a_num > a_guess:
        print("Too low.")
        return True
    else:
        print(f"You got it! The answer was {a_num}")
        return False

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

hidden_number = random.randint(1, 100)

difficulty = input("Choose a dificulty. Type 'easy' or 'hard': ")


if difficulty == 'easy':
    player_lives = 10
else:
    player_lives = 5


while True:
    print(f"You have {player_lives} attempts remaining to guess the number")
    guessed_number = int(input("Make a guess: "))
    if check_score(hidden_number, guessed_number):
        player_lives -= 1
        if player_lives == 0:
            print("You've run out of guesses, you lose.")
            break
        else:
            continue
    else:
        break
