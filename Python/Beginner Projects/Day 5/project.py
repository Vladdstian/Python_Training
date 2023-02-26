import random
import string

def get_user_input(input_type: str) -> int:
    while True:
        user_input = input(f"How many {input_type} would you like in your password? ")
        try:
            user_input = int(user_input)
            return user_input
        except ValueError:
            print("Please enter a valid number.")

def generate_password(length: int, letters: str, symbols: str, numbers: str) -> str:
    password_chars = []
    password_chars.extend(random.sample(letters, get_user_input("letters")))
    password_chars.extend(random.sample(symbols, get_user_input("symbols")))
    password_chars.extend(random.sample(numbers, get_user_input("numbers")))
    password_chars.extend(random.sample(string.ascii_letters + string.digits, length - len(password_chars)))
    random.shuffle(password_chars)
    return "".join(password_chars)

def main():
    letters = string.ascii_letters
    symbols = "!#$%&()*+"
    numbers = string.digits
    length = get_user_input("length")
    password = generate_password(length, letters, symbols, numbers)
    print(f"\nYour password is: {password}.")

if __name__ == "__main__":
    main()
