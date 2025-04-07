def add_three_copies(list,data):
    for i in range(3):
        list.append(data)
def main():
    message = input(" enter a message to copy. ")
    list = []
    print("Before list:",list)
    add_three_copies(list,message)
    print("After list", list)
if __name__ == "__main__":
    main()