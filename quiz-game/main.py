from question_model import Question
from data import question_data
from quiz_brain import Brain

ques_bank = []

for i in range(len(question_data)):
    q_obj = Question(question_data[i]["question"], question_data[i]["correct_answer"])
    ques_bank.append(q_obj)

quiz = Brain(ques_bank)

while quiz.still_have_ques():
    quiz.next_ques()

print("\nCongratulations!! You have completed the quiz.")
print(f"Your score is {quiz.score}/{quiz.ques_num}")

