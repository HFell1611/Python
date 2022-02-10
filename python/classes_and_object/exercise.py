class Student():
    student = {}
    def __init__(self, name, age, class_ = "student"):
        self.name = name
        self.age = age
        self.class_ = class_
        if self.class_ in Student.student:
            Student.student[class_].append(self)
        else:
            Student.student[class_] = [self]
        Student.student.append(self)

    def mark(self, sc1, sc2, sc3):
        return  (sc1 + sc2 + sc3)/3

    def __str__(self):
       return f"A student called {self.name}"


# name = input("Entar a name: ")
# age = int(input("Enter an age: "))
# newstudent = Student(name,age)

student1 = Student('Bob', 20, 'history')
student2 = Student('Alice', 23 , 'geography')
student3 = Student('Derek', 19, 'history')

# for k , v in Student.student.items():
#     print(f"Students studying {k}: {[str(s) for s in v]}")

print(dir(student1))