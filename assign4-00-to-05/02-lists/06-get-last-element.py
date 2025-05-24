def get_last_element(list):
    print(list[-1])
    
def get_list():
    list = []
    elem:str = input("enter an element to add to the list.")
    while elem != "":
        list.append(elem)
        elem = input("inter an element to add to the list")
    return list

def main():
    list = get_list()
    get_last_element(list)
    
if __name__=="__main__":
    main()