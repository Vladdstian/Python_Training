from quiz import QuizBrain, Question
from replit import clear

print("Welcome to the Quiz Master 1000!\n")
user_question_number = int(input("How many questions would you like to try?: "))
user_difficulty = input("What about the difficulty? type 'easy'/ 'medium'/ 'hard': ")

game = QuizBrain(user_question_number, user_difficulty)
game_on = True

while game.still_has_questions():
    game.next_question()

print(f"You finished the game! Your final score is {game.score}/{game.q_number}")
