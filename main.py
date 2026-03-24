from data import question_data
from question_model import Question
from quiz_brain import Game

question_bank = [ ]
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    question_bank.append(Question(question_text, question_answer))

quiz = Game(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz..!")
print(f"Your Final score is {quiz.score}/{quiz.question_number}...")
