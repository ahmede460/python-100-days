import random 


names = ['ahmed', 'ali', 'mohd', 'fatema']

dict_students = {name:random.randint(1,100) for name in names}

print(dict_students)

passed_students = {student:score for (student, score) in dict_students.items() if score > 50}

print(passed_students)