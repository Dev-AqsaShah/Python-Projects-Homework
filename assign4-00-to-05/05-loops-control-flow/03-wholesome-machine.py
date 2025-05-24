correct_affermation = "i am capable of doing anything. i pet my mind too."

def main():
    print("Welcome to the wholesome machine")
    while True:
        user_input = input("please type the following afformation:") + correct_affermation
        if user_input == correct_affermation:
            print("thats right")
            break
        else:
            print("hmm that was not the offermation. try again:")
        
        if __name__ == "__main__":
            main()