# 1. Using self
# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.



class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
    def display(self):
        print(f'Name: {self.name}, Marks: {self.marks}')
        
Student1:Student = Student("AQSA shah", 95)
Student2:Student = Student("unknown", 85)
print("Student 1 Details:",Student1.display())
print(Student1.name,Student1.marks)
print("Student 2 Details:", Student2.display())
    