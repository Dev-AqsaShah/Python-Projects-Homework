# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "ABC Bank"
    
    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name
        
b1:Bank = Bank()
print(b1.bank_name)
b2:Bank = Bank()
print(b2.bank_name)
Bank.change_bank_name("XYZ Bank")
print(b1.bank_name)
print(b2.bank_name)



# 5. Static Variables and Static Methods
# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.

class MathUtils:
    @staticmethod
    def add(a,b):
        return a + b
    
    print(MathUtils.add(5,10))  # noqa: F821



# 6. Constructors and Destructors
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).


class Logger:
    def __init__(self):
        print("Logger object created.") 
        
    def __del__(self):
        print("Logger object destroyed.")
        
log:Logger = Logger()
del log


# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.


class Employee:
    def __init__(self,name,salary,ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn
        
emp1 : Employee = Employee("aqsa shah",50000,"123-45-678")
print(emp1.name) 
print(emp1._salary)
print(emp1.__ssn)



# 8. The super() Function
# Assignment:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.


class Person:
    def __init__(self,name):
        self.name = name
        
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        
teacher: Teacher = Teacher("aqsa shah", "computer science")  # noqa: F821
print(f'Name: {teacher.name}, Subject: {teacher.subject}')


# 9. Abstract Classes and Methods
# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self,heigh,width):
        self.height = height  # noqa: F821
        self.width = width
        
    def area(self):
        return self.height * self.width
    
rect1 :Rectangle = Rectangle(5.10)
print(f'area of rectangle: {rect1.area()}')



# 10. Instance Methods
# Assignment:
# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.

class Dog:
    def __init__(self,name,bread):
        self.name = name
        self.bread = bread
    def bark(self):
        print(f'{self.name} says wooff')
        
dog :Dog = Dog("Tommy","labrador")
print(dog.bark())