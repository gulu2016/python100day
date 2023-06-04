class QuizBrain:
    def __init__(self,question_bank):
        self.question_num = 0
        self.question_bank = question_bank
        self.score = 0

    def still_have_questions(self):
        if self.question_num < len(self.question_bank):
            return True
        else:
            return False

    def next_question(self):
        # s158-1-1-1 使用类内的属性需要带上self
        current_question = self.question_bank[self.question_num]
        currect_answer = current_question.answer
        self.question_num += 1
        # s158-1-1-2 input函数可以获取用户的输入之前，先输出一些信息
        # s158-1-1-3 f开头的字符串中可以使用一些变量
        user_answer = input(f"Q.{self.question_num}:{current_question.text} (True/False): ")
        self.check_answer(user_answer,currect_answer)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("you got rignt")
            self.score += 1
        else:
            print("you got wrong")
        print(f"correct answer is {correct_answer}")
