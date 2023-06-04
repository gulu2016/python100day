from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# s157-1-1-1 将question数据加载为对象
question_bank = []
for item in question_data:
    question = Question(item["text"], item["answer"])
    question_bank.append(question)

quizBrain = QuizBrain(question_bank)
while quizBrain.still_have_questions():
    quizBrain.next_question()

print(f"total score is {quizBrain.score}")
