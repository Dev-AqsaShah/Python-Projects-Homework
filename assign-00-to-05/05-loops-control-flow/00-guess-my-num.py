import random  # Added missing import

def main():
    secret_number = random.randint(1, 100)  # Fixed typo: readint → randint
    print("I am thinking of a number between 1 and 100...")
    
    guess = int(input("Enter a guess: "))  # Added space for better UX
    
    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low.")  # Fixed typo: guest → guess
        else:
            print("Your guess is too high.")
        guess = int(input("Enter a guess: "))  # Added space for better UX
        
    print("You got it!")  # Fixed indentation (was inside while loop)

# Added call to main function
if __name__ == "__main__":
    main()