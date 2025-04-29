
my_list = ["apple", "mango", "orange", "peer", "peach"]
def access_element(my_list,index):
    """return the element at the specified index, or on error message if out of range."""
    if 0 <= index < len(my_list):
        return f"element at index {index}: {my_list{index}}"
    return "index out of range"

def modify_element(my_list,index,new_value):
    """modifies the element at the specified index with the new value."""
    if 0 <= index < len(my_list):
        old_value = my_list[index]
        my_list[index] = new_value
        return f"element at index {index} modified from {old_value} to {new_value}"
    return "index out of range"

def slice_list(my_list,start,end):
    """returns a new list containing the elements from the start index to the end index (exclusive)"""
    if 0 <= start < len(my_list) and 0 <= end <= len(my_list):
        return f"sliced list: {my_list[start:end]}"
    return("invalid slice indicates")

def list_game():
    print("\n welcome to the list manipulation")
    
    my_list =  ["apple", "mango", "orange", "pear", "peach"]
    while True:
        print("current list", my_list)
        
    print("select an operation")
    print("1, access element")
    print("2, modify element")
    print("3, slice list")
    print("4, quit")
    
    choice = input("enter your choice (1-4)")

