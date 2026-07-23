def check_balance(balance):
    print(f"Your Current Balance: BDT {balance}\n")

def deposit(balance):
    while True:
        try:
            amount = float(input("Enter Amount: "))
        except ValueError:
            print(f"Invalid Amounnt. Try again.")
            continue

        if amount <= 0:
            print("Invalid Amount. Try again.")
            continue

        balance += amount
        print(f"BDT.{amount} deposited successfully.")
        print(f"Current Balance: BDT {balance}\n")
        return balance

def withdraw(balance):
    while True:
        try:
            amount = float(input("Enter Amount: "))
        except ValueError:
            print(f"Invalid Amounnt. Try again.")
            continue

        if amount > balance:
            print("Insufficient Balance")
            continue
        if amount <= 0:
            print("Invalid Amount.")
            continue

        balance -= amount
        print(f"BDT.{amount} withdrawn successfully.")
        print(f"Current Balance: BDT {balance}\n")
        return balance

    


balance = 5000
exit_programme = False
print("\n=====Main Menu=====")

while True:
    try:
        selected_opt = int(input(f"1. Check Balance\n"
                                  "2. Deposit\n"
                                  "3. Withdraw\n"
                                  "4. Exit\n"
                                  "Please, Select an option: "))
    except ValueError:
        print(f"Invalid Input. Try again.\n")
        continue

    if selected_opt < 1 or selected_opt > 4:
        print(f"Invalid Input.\n")
        continue

    
    else:
        if selected_opt == 1:
            check_balance(balance)

        elif selected_opt == 2:
            balance = deposit(balance)
            continue

        elif selected_opt == 3:
            balance = withdraw(balance)
            continue

        else:
            options = ("y", "n")
            while True:
                opt = input(f"Are you sure you want to exit? (y/n): ").lower()
                if opt in options:
                    if opt == "y":
                        exit_programme = True
                        break
                    else:
                        print("Returning to Main Menu...\n")
                        exit_programme = False
                        break
                else:
                    print("Invalid Input.")

    if exit_programme:
        break

    
           