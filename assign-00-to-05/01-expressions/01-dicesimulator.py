import random
def roll_dice():
    dice1:int = random.randint(1,6)
    dice2:int = random.randint(1,6)
    total:int = dice1 + dice2
    print(f'total of two dice: {total}')
    
def main():
    dice1:int = 10
    print("dice1 in main() start as:" + str(dice1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("dice1 in main() is: " + str(dice1))
    
if __name__ == "__main__":
    main()