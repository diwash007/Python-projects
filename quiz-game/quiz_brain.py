class Brain:
    def __init__(self, ques_list):
        self.ques_num = 0
        self.ques_list = ques_list
        self.score = 0
    
    def check_answer(self,uans, ans):
        if uans.lower() == ans.lower():
            print("You got it right!!")
            self.score += 1
        else:
            print("Incorrect answer!!")
        print(f"The answer was: {ans}")
        print(f"Your score: {self.score}/{self.ques_num}\n")


    def next_ques(self):
        curr_question = self.ques_list[self.ques_num]
        self.ques_num +=1
        Uans = input(f"Q.{self.ques_num}. {curr_question.ques}\n(True or False?) : ")

        self.check_answer(Uans, curr_question.ans)
    
    def still_have_ques(self):
        return self.ques_num < len(self.ques_list)
            