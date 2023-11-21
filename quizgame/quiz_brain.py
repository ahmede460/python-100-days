class QuizBrain:


    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        

    def next_question(self):
        user_answer =input(f"Q.{self.question_number + 1 } - {self.question_list[self.question_number].question} True or False? : ")
        correct_answer = self.question_list[self.question_number].answer
        self.checkanswer(user_answer,correct_answer)
        self.question_number += 1
        
    def still_has_questions(self):
        if self.question_number == len(self.question_list):
            print(f"Your final score is {self.score}/{len(self.question_list)} 😂")
            return False
        else:
            return True
    
    def checkanswer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Your answer is correct ! you go it right ✅")
            self.score += 1
            
        else:
            print("That's Wrong ❌")           
        print(f"You score is {self.score}/{self.question_number + 1}")