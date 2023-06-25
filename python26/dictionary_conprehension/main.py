import random

name = ['Alex','Beth','Caroline','Dave','Eleanor','Freddie']

#s238-1-1-1 使用字典的简易方法构造字典
students_scores = {student:random.randint(0,100) for student in name}
print(students_scores)

#s238-1-1-2 使用字典的简易方法构造字典，同时添加构造条件
passed_students = {student:score for (student,score) in students_scores.items() if score >= 60}
print(passed_students)
