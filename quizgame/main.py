from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank  = []
for each_question in question_data:
  q =(each_question["text"])
  a = (each_question["answer"])
  newquestion = Question(q,a)
  question_bank.append(newquestion)
  

myquizbrain = QuizBrain(question_bank)

endofgame = True

while endofgame != False:
    myquizbrain.next_question()
    endofgame = myquizbrain.still_has_questions()
    