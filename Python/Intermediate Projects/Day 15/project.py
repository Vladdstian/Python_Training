MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money_inside_machine = 0

def payment_processing(total):
    total_payed = 0
    print(f"\nTotal to be payed: ${total}.")
    while total_payed != total:
        pennies = int(input("Please insert pennies: ")) * 0.01
        nickels = int(input("Please insert nickels: ")) * 0.05
        dimes = int(input("Please insert dimes: ")) * 0.1
        quarters = int(input("Please insert quarters: ")) * 0.25
        total_payed = total_payed + pennies + nickels + dimes + quarters
        if total_payed < total:
            print(f"You only payed ${total_payed}. You still have to pay ${(total-total_payed):.2f}.")
            additional = input('Would you like to add more? "Y" or "N" : ').upper()
            if additional == "Y":
                continue
            print(f"${total_payed} has been refunded. Thank you!")
            return False
        elif total_payed > total:
            print(f"You payed too much! Here is the rest ${(total_payed-total):.2f}. Thank you!")
            return True
        else:
            return True


def report():
    print("Here are the resources status for this coffee machine: ")
    for key in resources:
        print(f"{key.title()}: remaining {resources[key]} (ml/g)")
    print(f"Money: ${money_inside_machine}")


def check_resources(ingredients):
    for item in ingredients:
        if ingredients[item] < resources[item]:
            continue
        print(f"Sorry there is not enought {item}. Please refill!")
        return False
    return True


def create_drink(drink):
    for item in drink['ingredients']:
        resources[item] -= drink['ingredients'][item]
    global money_inside_machine
    money_inside_machine += drink['cost']


machine_is_on = True
resources
while machine_is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "report":
        report()
        continue
    elif user_choice == 'off':
        print("Powering off...")
        break
    elif user_choice in MENU:
        if check_resources(MENU[user_choice]['ingredients']):
            if payment_processing(MENU[user_choice]['cost']):
                create_drink(MENU[user_choice])
                print(f"Here is your {user_choice}. Enjoy!")
                continue
    else:
        print(f"I'm sorry but the machine doesn't have {user_choice}.")
        print("Please try again!")
        continue

