ATM Simulation in Python 

# Overview 

This is a simple terminal-based ATM simulation program written in Python. Users can securely perform typical ATM functions—such as withdrawing funds, depositing money, checking balance, and exiting the session—using secure PIN verification before each transaction. 

# Features 

Secure PIN verification before every transaction 

Withdraw money with balance checking 

Deposit money to increase account balance 

View current account balance 

Graceful exit from the program 

Usage Instructions 

Run the Script: 
Execute the Python script in your terminal or IDE. 

Interact with the Menu: 
The program presents a menu with four options: 

Withdraw 

Deposit 

Check Balance 

Exit 

Enter the number (1-4) corresponding to your chosen action. 

# PIN Verification: 
Before performing any operation, you will be asked to enter your PIN. If correct, the transaction proceeds; otherwise, you'll receive an error message and return to the main menu. 

# Withdraw / Deposit Rules: 

For withdraw: If the requested amount exceeds the current balance, you'll receive an insufficient balance notice. 

For deposit: The entered amount gets added to your balance. 

Exit: 
Selecting "Exit" displays a farewell message and ends your session. 

# Example Session 

text 

===== ATM MENU ===== 
1. Withdraw 
2. Deposit 
3. Check Balance 
4. Exit 
Enter your choice (1-4): 1 
Enter your PIN: 2341 
Enter amount to withdraw: 1000 
Withdrawal Successful! Amount withdrawn: 1000 
Available Balance: 9000 

 
