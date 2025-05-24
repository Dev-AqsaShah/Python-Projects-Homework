inch: int = 12

def foot():
    feet: int = int(input("enter feet and i will convert into inchs."))
    print(f'there are {inch * feet} inches in {feet} feet.')
    
if __name__ == "__main__":
    foot()