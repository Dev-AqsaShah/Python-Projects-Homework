def main():
    secret_number = random.readint(1,100)
    print("i am thinking of a number between 1 and 100...")
    
    guess = int(input("enter a guess:"))
    
    while guess != secret_number: