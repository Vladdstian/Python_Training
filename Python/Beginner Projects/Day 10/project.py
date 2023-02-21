from art import logo
from replit import clear

def addition(a, b):
    return a+b

def subtraction(a, b):
    return a-b

def multiplication(a, b):
    return a*b

def division(a, b):
    return a/b

operations = {
        "+": addition,
        "-": subtraction,
        "*": multiplication,
        "/": division
        }

continue_calc = True

while continue_calc:
    print(logo)
    first_num = int(input("What's the first number?: "))
    while True:
        operation_choice = input(f"Pick an operation {' '.join([key for (key, value) in operations.items()])}: ")
        second_num = int(input("What's the next number?: "))
        result = operations[operation_choice](first_num, second_num)
        equation_as_str = str(first_num) + " " + operation_choice + " " + str(second_num) + " = " + str(result)
        print(equation_as_str)
        continue_calculations = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation.")
        if continue_calculations == 'y' or continue_calculations == 'yes':
            clear()
            print(logo)
            first_num = result
            continue
        else:
            break
    clear()
