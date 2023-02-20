import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', '^Z^Zg', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the password generator!\n")

def check(type_of_char: str, list_of_char: list):
    list_of = []
    while True:
        no_of = input(f"How many {type_of_char} would you like in your password? ")      
        try:
            no_of = int(no_of)
        except:
            print("Please enter a valid number.")
            continue
        break
    for nom in range(no_of):
        list_of.append(random.choice(list_of_char))
    return list_of

no_of_letters = check("letters", letters)
no_of_symbols = check("symbols", symbols)
no_of_numbers = check("numbers", numbers)

password_chars = no_of_letters + no_of_symbols + no_of_numbers
random.shuffle(password_chars)
password = ''.join(password_chars)

print(f"\n\nYour password is: {password}.")

