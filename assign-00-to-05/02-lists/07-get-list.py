def main():
    list = []
    value = input("enter a value to add to the list. ")
    while value:
        list.append(value)
        value = input("enter a value to add to the list.")
    print("here's the list:", list)

if __name__ == "__main__":
    main()