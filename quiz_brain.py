import random

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        q_list = self.question_list
        current_question = q_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}. {current_question.text} | (True or False): ")
        if user_answer.lower() == current_question.answer.lower():
            self.score += 1
            print("CORRECT!")
            print(f"Your current score is: {self.score} / {self.question_number}")
            print("\n")
        else:
            print(f"WRONG! The correct answer is: {current_question.answer}")
            print(f"Your current score was: {self.score} / {self.question_number}")
            print("\n")

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            print("\n******** You've reached the end of the Quiz! ********")
            print(f"******** Your final score is {self.score} out of {self.question_number}. Good job! ********")
