import random
print("high low game")

round = 5

def main():
    print("welcome to the high low game")
    print("***********************")
    
    your_score = 0
    
    for i in range(round):
        print("round", i + 1)
        
        computer_number : int = random.randint(1.100)
        your_number:int = random.randint(1,100)
        print("your number is", your_number)
        
        choice:str = input("do you think your number is higher or lower than the computers numbr ")
        higher_and_correct:bool = choice == "higher" and your_number > computer_number
        lower_and_correct:bool = choice == "lower" and your_number < computer_number
        
        if higher_and_correct or lower_and_correct:
            print("you were right the computer num was", computer_number)
            score += 1  # noqa: F821
        else:
            print("thats incorrect the computer num was", computer_number)
            
            print("your score is now",score)
            print()
            
        print("thanks for playing:")
        
        if __name__ == "__main__":
            main()