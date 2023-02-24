import requests
import json

class Question:
    """
    A class that is used for creating a question object.

    Attributes:
        question_text (str): The actual text of the question.
        correct_answer (str): The correct answer for the question text.

    Methods:
        __init__(self, question_text, correct_answer): Constructor method that creates a question object based on the input provided.
    """

    def __init__(self, question_text, correct_answer):
        self.text = question_text
        self.answer = correct_answer


class QuizBrain:
    """
    A class for creating a new quiz game based on user preferences.

    Attributes:
        questions_num (int): The number of questions desired by the player.
        difficulty (str) -> easy/medium/hard: This changes the difficulty of the questions
        questions (list): A list that contains the desired number of Question objects.
    
    Methods:
        __init__(self, questions_num, difficulty): Constructor method that sets the initial values for the classes attributes.
                                                   As default the number of questions is set to 10 and the difficulty to 'easy'.  
        __update_question_list(self): It runs automatically when creating a new Quiz game and uses the 'requests' module to update the list of questions.
        next_question(self): It returns and removes the next question from the class questions list.

    """

    def __init__(self, questions_num=10, difficulty='easy'):
        self.questions_amount = questions_num
        self.difficulty = difficulty
        self.score = 0
        self.q_number = 0
        self.q_bank = []
        self.__update_q_bank()

    def __update_q_bank(self):
        api_endpoint = f"https://opentdb.com/api.php?amount={self.questions_amount}&difficulty={self.difficulty}&type=boolean"
        data = requests.get(api_endpoint)
        data = data.json()['results']
        for item in data:
            question_text = item['question'] 
            correct_answer = item['correct_answer']
            self.q_bank.append(Question(question_text, correct_answer))
        
    def next_question(self):
        current_question = self.q_bank[self.q_number]
        self.q_number += 1
        user_answer = input(f"\n\nQ.{self.q_number}: {current_question.text}. (True/False)?: ").lower()
        self.check_answer(user_answer, current_question.answer)
        print(f"Your score is {self.score}/{self.q_number}.")

    def still_has_questions(self):
        return self.q_number != len(self.q_bank)

    def check_answer(self, u_answer, q_correct_answer):
        if u_answer == q_correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("Wrong answer!")
        print(f"The correct answer was: {q_correct_answer}")
