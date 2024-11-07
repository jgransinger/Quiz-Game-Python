from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    new_q_text = question["text"]
    new_q_answer = question["answer"]
    new_q = Question(new_q_text, new_q_answer)
    question_bank.append(new_q)

newQuiz = QuizBrain(question_bank)

while newQuiz.still_has_questions():
    newQuiz.next_question()