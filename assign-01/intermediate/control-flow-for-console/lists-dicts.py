my_list = ["apple", "mango", "orange", "pear", "peach"]

def access_element(my_list, index):
    """Return the element at the specified index, or an error message if out of range."""
    if 0 <= index < len(my_list):
        return f"Element at index {index}: {my_list[index]}"
    return "Index out of range."

def modify_element(my_list, index, new_value):
    """Modify the element at the specified index with the new value."""
    if 0 <= index < len(my_list):
        old_value = my_list[index]
        my_list[index] = new_value
        return f"Element at index {index} modified from {old_value} to {new_value}"
    return "Index out of range."

def slice_list(my_list, start, end):
    """Return a new list containing the elements from the start index to the end index (exclusive)."""
    if 0 <= start < len(my_list) and 0 <= end <= len(my_list):
        return f"Sliced list: {my_list[start:end]}"
    return "Invalid slice indices."

def list_game():
    print("\nWelcome to the List Manipulation Game!")

    my_list = ["apple", "mango", "orange", "pear", "peach"]

    while True:
        print("\nCurrent list:", my_list)
        print("Select an operation:")
        print("1. Access element")
        print("2. Modify element")
        print("3. Slice list")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            try:
                index = int(input("Enter the index of the element you want to access: "))
                print(access_element(my_list, index))
            except ValueError:
                print("Please enter a valid integer index.")
        elif choice == "2":
            try:
                index = int(input("Enter the index of the element you want to modify: "))
                new_value = input("Enter the new value for the element: ")
                print(modify_element(my_list, index, new_value))
            except ValueError:
                print("Please enter a valid integer index.")
        elif choice == "3":
            try:
                start = int(input("Enter the start index for the slice: "))
                end = int(input("Enter the end index for the slice: "))
                print(slice_list(my_list, start, end))
            except ValueError:
                print("Please enter valid integer indices.")
        elif choice == "4":
            print("Exiting the game. Thanks for playing!")
            break
        else:
            print("Invalid choice. Enter a number between 1 to 4.")

if __name__ == "__main__":
    list_game()
