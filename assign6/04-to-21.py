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