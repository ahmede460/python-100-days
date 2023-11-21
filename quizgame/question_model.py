import random
from data import question_data

class Question:
    def __init__(self, question, answer):
        '''Initiating the question by adding two attributes anwer and question'''
        #self.question_id = question_id
        self.question = question
        self.answer = answer
