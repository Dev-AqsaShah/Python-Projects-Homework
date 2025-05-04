import random 
print("welcome to the number guessing game!")

secret_number = random.randint(1, 10)
print("i have secret number between 1 and 10. can you guess it?")

while True:
    try:
        guess = int(input("enter your guess:"))
        if guess > secret_number:
            print("too high try again.")
        elif guess < secret_number:
            print("too low try again.")
        else:
            print("congratulations you have guessed the number")
            break
    except ValueError:
        print("invalid input please enter a number between 1 and 10.")
