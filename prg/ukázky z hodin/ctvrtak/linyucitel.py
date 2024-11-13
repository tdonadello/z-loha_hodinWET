import random

student = input("What is your name? ")

if student.lower == "Dony":
    mark_options = [1, 1, 2, 3, 4]
    random_mark = random.choice(mark_options)
    
else:
    random_mark = random.randint(1, 5)
    
print(random_mark)
