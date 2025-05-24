import random

print("Welcome to the Number Guessing Game!")
print("Think of a number between 1 and 10, and the computer will try to guess it.")

low = 1
high = 10

while low <= high:
    guess = random.randint(low, high)
    print("Computer's guess is:", guess)

    feedback = input("Is the guess too high (H), too low (L), or correct (C)? ").strip().upper()

    if feedback == "C":
        print("Yay! The computer guessed your number.")
        break
    elif feedback == "H":
        high = guess - 1
    elif feedback == "L":
        low = guess + 1
    else:
        print("Invalid input. Please enter H, L, or C.")

if low > high:
    print("Hmm, it seems like something went wrong. Are you sure you followed the rules?")
