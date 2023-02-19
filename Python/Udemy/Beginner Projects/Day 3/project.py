import random


print("""           
                           _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
               '-._'-.|| |' `_.-'
                    '-.||_/.-'

""")
print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure chest! Good luck adventurer!")
while true:
    choice_1 = input("You find yourself on an island, on the beach. In front of you is a dark forest. Will you go explore it or take a walk on the beach? ").lower()

    if choice_1 == 'explore' or choice_1 == 'dark' or choice_1 == 'forest':
        continue
    else:
        print("A giant crab comes out of the sand. You haven't seen anything this big. Untill you realise, it grabs you and...")
        print("GAME OVER")
        break

    print("The dark forest is a magical place and you hear lots of unknown  noises. You go further and deep inside the jungle you see a lake. The water is muddy and you cannot see anything.")

    choice_2 = input("Will you swim to advance or take a stroll and go around it? ").lower()

    if choice_2 == "swim":
        print("The lake is filled with hungry pirhanas.")
        print("Somebody else will have to go find the treasure ... GAME OVER!")
        break
    
    print("You decide to take the long route and it pays off. In the distance you see something that looks like a big wall.")

    choice_3 = input("You run quickly and find 3 doors: a red door, a blue door and a yellow door. Which one will you try? ").lower()

    treasure_door = random.choice(["red", "blue", "yellow"])
    print(treasure_door)
    if choice_3 == treasure_door:
        print("In front of you appears a treasure chest shinny as the sun!")
        print("It is so bright that attracts the attention of nearby planes and so you are saved!")
        print("You win! Well done adventurer!")
    else:
        print(f"Once opening the {choice_3} door, you hear a very unsettling noise. Nothing good comes out after...")
        print("Game Over!Better luck next time!")
        break

