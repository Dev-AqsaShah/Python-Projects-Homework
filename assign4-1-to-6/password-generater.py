import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

length = int(input("enter the desired password length:"))

if __name__ == "__main__":
    print("generate password",(length))