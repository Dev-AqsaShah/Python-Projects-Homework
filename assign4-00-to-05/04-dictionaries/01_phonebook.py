from typing import Dict

def add_contact(phonebook: Dict[str, str]) -> None:
    name: str = input("Enter contact name: ")
    number: str = input("Enter contact number: ")
    
    if name in phonebook:
        print(f"{name} already exists in the phonebook")
    else:
        phonebook[name] = number
        print(f"{name} added to the phonebook.")

def search_contact(phonebook: Dict[str, str]) -> None:
    name: str = input("Enter contact name to search: ")
    
    if name in phonebook:
        print(f"{name}: {phonebook[name]}")
    else:
        print(f"{name} not found in the phonebook.")

def delete_contact(phonebook: Dict[str, str]) -> None:
    name: str = input("Enter contact name to delete: ")
    if name in phonebook:
        del phonebook[name]
        print(f"{name} deleted from the phonebook.")
    else:
        print(f"{name} not found in phonebook.")

def display_contact(phonebook: Dict[str, str]) -> None:
    if phonebook:
        print("\nPhonebook contacts list:")
        for name, number in phonebook.items():
            print(f"{name}: {number}")
    else:
        print("Phonebook is empty.")

if __name__ == "__main__":
    phonebook: Dict[str, str] = {}
    
    while True:
        print("\nPhonebook Menu")
        print("1. Add contact")
        print("2. Search contact")
        print("3. Delete contact")
        print("4. Display contacts")
        print("5. Exit")
        
        choice: str = input("Enter your choice (1-5): ")
        
        if choice == "1":
            add_contact(phonebook)
        elif choice == "2":
            search_contact(phonebook)
        elif choice == "3":
            delete_contact(phonebook)
        elif choice == "4":
            display_contact(phonebook)
        elif choice == "5":
            print("Exiting phonebook. Goodbye!")
            break
        else:
            print("Invalid choice. Enter a number between 1 to 5.")