balance = 10000   
PIN = "2341"      

def verifypin():
    userpin = input("Enter your PIN: ")
    if userpin == PIN:
        return True
    else:
        print("Incorrect PIN")
        return False

while True:
    print("\n===== ATM MENU =====")
    print("1. Withdraw") 
    print("2. Deposit")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        if verifypin():
            amount = int(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient Balance!")
            else:
                balance -= amount
                print(f"Withdrawal Successful! Amount withdrawn: {amount}")
            print(f"Available Balance: {balance}")

    elif choice == "2":
        if verifypin():
            amount = int(input("Enter amount to deposit: "))
            balance += amount
            print(f"Deposit Successful! Amount deposited: {amount}")
            print(f"Available Balance: {balance}")

    elif choice == "3":
        if verifypin():
            print(f"Your Current Balance: {balance}")

    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid Choice! Please choose between 1-4.")
