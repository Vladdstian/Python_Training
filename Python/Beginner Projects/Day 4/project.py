import random

print("Welcome to Rock, Paper, Scissors Game!\n")

choices = ["Rock", "Paper", "Scissors"]
score_player = 0
score_computer = 0

while True:
    player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
    computer_choice = random.randint(0,2)
    
    try:
        player_choice = int(player_choice)
    except:
        print("Please enter a valid choice!\n")
        continue

    print(f"Player chooses {choices[computer_choice]} and Computer chose {choices[computer_choice]}.\n")

    if player_choice == computer_choice:
        print("It's a Draw!")
        print("Next Round!\n")
    elif (player_choice == 0 and computer_choice== 2) or player_choice > computer_choice:
        score_player += 1
        print("Player winns this round!")
        print("Next Round!\n")
    elif (computer_choice == 0 and player_choice == 2) or computer_choice > player_choice:
        score_computer += 1
        print("Computer winns!") 
        print("Next Round!\n")
    
    print("The score is:")
    print(f"Player {score_player} - {score_computer} Computer\n")

    if score_player == 3:
        print("Player Wins!")
        break
    elif score_computer == 3:
        print("Computer Wins!")
        break
    else: 
        continue

