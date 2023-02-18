print("Welcome to the Band Name Generator software!\n\n")
birth_city = input("What is the city you were born in? ").lower().title()
pet_name = input("What is your pet name? ").lower().title()

if pet_name[-1] != 's':
    pet_name = pet_name + 's'


print(f"Your Band name could be: {birth_city + ' ' + pet_name}")
