# In a new Python file, create a class of students. It should contain the 
# following attributes: name, age, and class with default value "student".
# It should also contain a method which takes in 3 test scores and prints 
# the students average test score.

class Students():
    students = {} # tracking student objects in a dictionary
    def __init__(self, name, age, class_ = "student"):
        self.name = name
        self.age = age
        self.class_ = class_
        if self.class_ in Students.students:
            Students.students[class_].append(self) # add self to list of students in class_ if class_ is already in the dictionary
        else:
            Students.students[class_] = [self] # add new class_ to dict with list containing current student
    
    def avg_score(self, score1, score2, score3):
        return (score1 + score2 + score3) / 3
    
    def __str__(self):
        return self.name


# name = input("Enter a name: ")
# age = int(input("Enter an age: "))
# newstudent = Students(name, age)
# print(newstudent.name, newstudent.age, newstudent.class_)
# print(newstudent.avg_score(82, 64, 30))

student1 = Students('Bob', 20, 'history')
student2 = Students('Alice', 23, 'history')
student3 = Students('Claire', 19, 'physics')

for k, v in Students.students.items():
    print(f"Students studying {k}: {[str(s) for s in v]}") # looping through the dict and printing the list of students in each class

print([attr for attr in dir(student1) if '__' not in attr]) # using dir() to get all attributes/methods of an object

print(getattr(student3, 'class_')) # getting student3's class_ attribute using getattr
setattr(student1, 'age', 21) # updating student1's age attribute using setattr
print(student1.age)