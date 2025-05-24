peturksbouipo : int = 16
stanlv:int = 25
mayengwa:int = 48

def main():
    age:int = int(input("how old are you"))
    if age >= peturksbouipo:
        print(f"your age is {age}. you are eligible to vote in paturksbuipo")
    else:
        print("you are eligible to vote in peturksbouipo")
    if age >= stanlv:
        print(f"your age is {age}. you are eligible to vote in stanlv")
    else:
        print(f"your age is {age} you are eligible to vote in stanlv")
    if age >= mayengwa: 
        print(f"your age is {age}. you are not eligible to vote in mayengwa")
    else:
        print(f"your age is {age} you are not eligible to vote in mayengwa")
        
    if __name__ == "__main__":
        main()