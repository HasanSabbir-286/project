import random
import string

options = ("y", "n")
letters = list(string.ascii_letters)
digits = list(string.digits)
symbols = list(string.punctuation)

def user_input():
    while True:
        try:
            pass_length = int(input("Enter the length of your Password: "))
        except ValueError:
            print("Invalid Input. Try again.")
            continue

        minimum_length = 0
        while True:
            add_number = input("Do you want to add numbers? (y/n): ").lower()
            if add_number in options:
                if add_number == "y":
                    minimum_length += 1
                break
            print("Invalid Input.")

        while True:
            add_symbols = input("Do you want to add symbols? (y/n): ").lower()
            if add_symbols in options:
                if add_symbols == "y":
                    minimum_length += 1
                break
            print("Invalid Input.")

        
        if pass_length <= 0 or pass_length < minimum_length:
            print("Invalid length. Try again.")
            continue

        return pass_length, add_number == "y", add_symbols == "y"
    
def generate_pass(length, include_number, include_symbol):
    password = []
    available = letters.copy()
    if include_number:
        available += digits
        password.append(random.choice(digits))
        length -= 1
    if include_symbol:
        available += symbols
        password.append(random.choice(symbols))
        length -= 1

    for i in range(length):
        password.append(random.choice(available))

    random.shuffle(password)
    password ="".join(password)
    return password

while True:
    pass_length, add_number, add_symbols = user_input()
    password = generate_pass(pass_length, add_number, add_symbols)
    print(f"Generated Password: {password}")

    another_password = input("Generate another password? (y/n): ").lower()
    
    while another_password not in options:
        print("Invalid Input.")
        another_password = input("Generate another password? (y/n): ").lower()
    
    if another_password == "n":
        break
        
        