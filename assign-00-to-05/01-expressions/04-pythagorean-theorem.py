import math

def triangle():
    ab:float = float(input("enter the length of the side ab"))
    ac:float = float(input("enter the length of the side ac"))
    bc:float = math.sqrt(ab**2 + ac**2)
    print(f"the length of bc (the hypothenus is: {bc})")
    
if __name__ == "__main__":
    triangle()