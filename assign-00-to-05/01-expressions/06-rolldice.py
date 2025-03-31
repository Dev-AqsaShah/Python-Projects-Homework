import random
def dice():
    die1:int = random.randint(1,6)
    die2:int = random.randint(1,6)
    total:int = int(die1 + die2)
    print("first die:" + str(die1))
    print("second die:" + str(die2))
    print(f"total of two dies : {total}")

if __name__ == "__main__":
    dice()