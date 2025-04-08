MAX_LENGTH: int = 3
def shorten(list):
    while len(list) > MAX_LENGTH:
        last_element = list.pop()
        print(last_element)
        
def get_list():
    list = []
    element = input("enter an element to add to the list:")
    while element != "":
        list.append(element)
        element = input("enter an element to add to the list ")
    return list
def main():
    list = get_list()
    shorten(list)
    
if __name__ == "__main__":
    main()