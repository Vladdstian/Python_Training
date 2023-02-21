import random
from hangman_words import word_list
from hangman_art import stages, logo

def letter_guess():
    while True:
        choice = input("\nPlease guess a letter: ")
        try:
            choice = str(choice).lower()
            if len(choice) > 1 or (not choice.isalpha()):
                raise "NotValid"
        except:
            print("Please enter a valid letter!\n")
            continue
        else:
            return choice


def check_game_status(lives, word):
    if lives == 0:
        print("You ran out of lives. GAME OVER!")
        return False
    if word.count('_') == 0:
        print("Congratulations! You guessed the word!")
        return True
    return True

chosen_word = random.choice(word_list)
chosen_word = [lettr for lettr in chosen_word]
hidden_chosen_word = ["_" for lettr in chosen_word]

print(logo)
game_lives = 6
game_is_on = True

while game_is_on:
    game_word = " ".join(hidden_chosen_word)
    print(f"\nThe word is: {game_word}")
    print(stages[game_lives])
    guess = letter_guess()
    try:
        index_of_lettr = chosen_word.index(guess)
    except ValueError:
        game_lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
    else:
        hidden_chosen_word[index_of_lettr] = chosen_word[index_of_lettr]
    game_is_on = check_game_status(game_lives, hidden_chosen_word)

