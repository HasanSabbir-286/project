import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "calc_history.json")


# -----------------------------
# Load Data
# -----------------------------

try:
    with open(FILE_NAME, "r") as file:
        data = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    data = {"calc_history": []}


# -----------------------------
# Save Data
# -----------------------------

def save_data():
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


# -----------------------------
# Input Validation
# -----------------------------


def take_input():
    while True:
        try:
            first_num = float(input("\nEnter First Number: "))
            break
        except ValueError:
            print("Invalid Input")

    while True:
        try:
            second_num = float(input("\nEnter Second Number: "))
            break
        except ValueError:
            print("Invalid Input")

    return first_num, second_num


def get_yes_no(message):
    while True:
        choice = input(message).strip().lower()

        if choice in ("y", "n"):
            return choice

        print("Please enter only y or n.")


# -----------------------------
# Main Menu
# -----------------------------

def main_menu():
    print("\n======= Calculator =======\n")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. View History")
    print("6. Clear History")
    print("7. Exit")


# -----------------------------
# Addition (+)
# -----------------------------

def addition():
    num1, num2 = take_input()
    print(f"{num1} + {num2} = {num1 + num2:.2f}")
    data["calc_history"].append(
        f"{num1} + {num2} = {num1 + num2:.2f}"
    )
    
    save_data()


# -----------------------------
# Subtraction (-)
# -----------------------------

def subtraction():
    num1, num2 = take_input()
    print(f"{num1} - {num2} = {num1 - num2:.2f}")
    data["calc_history"].append(
        f"{num1} - {num2} = {num1 - num2:.2f}"
    )
            
    save_data()


# -----------------------------
# Multiplication (*)
# -----------------------------

def multiplication():
    num1, num2 = take_input()
    print(f"{num1} * {num2} = {num1 * num2:.2f}")
    data["calc_history"].append(
        f"{num1} * {num2} = {num1 * num2:.2f}"
    )
            
    save_data()


# -----------------------------
# Division
# -----------------------------

def division():
    while True:
        num1, num2 = take_input()
        if num2 == 0:
            print("Cannot divide by 0.")
            continue

        print(f"{num1} / {num2} = {num1 / num2:.2f}")

        data["calc_history"].append(
            f"{num1} / {num2} = {num1 / num2:.2f}"
        )
                
        save_data()
        break

# -----------------------------
# View History
# -----------------------------

def view_history():
    print("\n======= Calculator History =======\n")
    if not data["calc_history"]:
        print("No calculation data available.")
        return
    for history in data["calc_history"]:
        print(history)


# -----------------------------
# Clear History
# -----------------------------

def clear_history():
        if not data["calc_history"]:
            print("\nNo calculation data available.")
            return

        choice = get_yes_no("Do you want to clear calculator history? (y/n): ")
        if choice == "y":
            

            data["calc_history"].clear()
            save_data()
            print("Calculation history cleared successfully.")
            return


# -----------------------------
# Main Function
# -----------------------------

def main():
    while True:
        main_menu()
        try:
            choice = int(input("Choose an option: "))
            if choice not in range(1, 8):
                print("Invalid Input.")
                continue
        except ValueError:
            print("Invalid Input.")
            continue
            
        if choice == 1:
            addition()
        elif choice == 2:
            subtraction()
        elif choice == 3:
            multiplication()
        elif choice == 4:
            division()
        elif choice == 5:
            view_history()
        elif choice == 6:
            clear_history()
        elif choice == 7:
            print("Thanks for using our calculator.")
            break
        
if __name__ == "__main__":
    main()