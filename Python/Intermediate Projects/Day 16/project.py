from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    user_choice = input(f"What would you like to drink? {menu.get_items()}: ")
    if user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_choice == "off":
        print("Powering off...")
        break
    else:
        order = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(order):
            if money_machine.make_payment(order.cost):
                coffee_maker.make_coffee(order)
                continue
