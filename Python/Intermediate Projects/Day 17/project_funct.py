import requests
import json

print("Welcome to Trivia Quest! Ready to test your knowledge?\n")
ammount = int(input("How many qustions would you like to try?: "))
difficulty = input("What about the difficulty? Type 'easy'/ 'medium' / 'hard': ")
api_endpoint = f"https://opentdb.com/api.php?amount={ammount}&difficulty={difficulty}&type=boolean"

data = requests.get(api_endpoint)
questions_list = data.json()['results']


score = 0
while len(questions_list) != 0:
    new_q = questions_list.pop()
    answer = input(new_q['question'] + " ").lower()
    if answer == new_q['correct_answer'].lower():
        score += 1
        print("You got it right!")
    else:
        print("Wrong!... moving forward ...")

print(f"Your final score: {score}")   
