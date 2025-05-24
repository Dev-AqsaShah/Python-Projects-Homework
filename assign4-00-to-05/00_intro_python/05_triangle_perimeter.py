def triangle():
    print("this code is about perimeter of triangle.")
    side1:float = float(input("enter your first side no of triangle."))
    side2:float = float(input("enter your second side no of triangle."))
    side3:float = float(input("enter your third side no of triangle."))
    total:float = float(side1 + side2 + side3)
    print(f'the perimeter of the triangle is {total}')
    
if __name__ == "__main__":
        triangle()
    