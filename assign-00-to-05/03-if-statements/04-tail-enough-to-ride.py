min_height: int = 50

def main():
    user: int = int(input("How tall are you? "))

    if user >= min_height:
        print("You are tall enough to ride!")
    else:
        print("You are not tall enough to ride, maybe next year.")

if __name__ == "__main__":
    main()
