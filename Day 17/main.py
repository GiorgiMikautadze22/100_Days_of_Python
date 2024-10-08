from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for data in question_data:
    question = data["question"]
    answer = data["correct_answer"]
    new_question = Question(question, answer)
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print('You have completed the quiz')
print(f'You final score is {quiz_brain.score}/{quiz_brain.question_number}')