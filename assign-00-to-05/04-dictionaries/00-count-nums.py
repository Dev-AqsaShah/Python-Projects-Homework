def count_numbers():
    count_dict = {}

    while True:
        num = input("Enter a number (or 'exit' to quit): ")

        if num.lower() == "exit":
            break

        if num.isdigit():
            num = int(num)
            count_dict[num] = count_dict.get(num, 0) + 1
        else:
            print("Invalid input. Please enter a number or 'exit'.")

    return count_dict

def display_counts(count_dict):
    print("\nNumber Counts:")
    for key, value in count_dict.items():
        print(f"{key} appears {value} times")

if __name__ == "__main__":
    counts = count_numbers()
    display_counts(counts)
