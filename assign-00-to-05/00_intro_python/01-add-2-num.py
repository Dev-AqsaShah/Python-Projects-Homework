def add():
    print("This application is for adding two numbers")
    first_number = int(input("Enter your first number: "))
    second_number = int(input("Enter your second number: "))
    total = first_number + second_number  # No need to cast total to int again
    print(f'The total sum of {first_number} and {second_number} is {total}')

if __name__ == "__main__":  # This should not be inside the function
    add()
