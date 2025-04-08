def get_first_element(my_list):
    print("First element:", my_list[0])

def get_list():
    my_list = []
    elam = input("Enter an element to add to the list (leave empty to stop): ")
    while elam != "":
        my_list.append(elam)
        elam = input("Enter an element to add to the list (leave empty to stop): ")
    return my_list

def main():
    user_list = get_list()
    if user_list:
        get_first_element(user_list)
    else:
        print("The list is empty.")

if __name__ == "__main__":
    main()


