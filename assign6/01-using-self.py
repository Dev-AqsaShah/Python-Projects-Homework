class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
    def display(self):
        print(f'Name: {self.name}, Marks: {self.marks}')
        
Student1:Student = Student("AQSA shah", 95)
Student2:Student = Student("Mosin shah", 85)
print("Student 1 Details:",Student1.display())
print(Student1.name,Student1.marks)
print("Student 2 Details:", Student2.display())
    