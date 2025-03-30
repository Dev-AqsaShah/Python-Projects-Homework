def reminder():
    num1:int = int(input("enter an integer to be divided: "))
    num2:int = int(input("enter an integer to divide by: "))
    question: int = num1 // num2
    reminder: int = num1 % num2
    print("the result of this division is " +str(question) + "with a reminder of " + str(reminder))
    
if __name__ == "__main__":
        reminder()
    