SBI

Problem Statement: Write a Python program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following: D 100 W 200 (Withdrawal is not allowed if balance is going negative. Write functions for withdraw and deposit) D means deposit while W means withdrawal.

2.Objectives:
Understand the concept of linear data structure “ARRAY” and how to declare & Use it. 
• Understand the concept of  different functions & how to declare ,define  & call it.
•	Understand the concept of list
•	Understand concept of function

3.Oucomes:
Python program that computes the net amount of a bank account based on a transaction log provided through console input. The program defines functions for depositing and withdrawing money, ensuring that withdrawals are not allowed if the balance would go negative.

•  Deposit Function: Adds the deposit amount to the current balance and returns the new balance.
•  Withdraw Function: Checks if there are sufficient funds for the withdrawal. If yes, it deducts the amount from the balance; otherwise, it prints an error message and returns the current balance.

•  Main Function:
Initializes the balance to zero.
--Reads the transactions from console input.
--Iterates through each transaction, splitting it into action and amount.
--Depending on the action (either "D" for deposit or "W" for withdrawal), it updates the balance accordingly.
--Finally, it prints the net balance

This ensures that the transactions are processed correctly and that withdrawals are only allowed if sufficient funds are available

4.Software and hardware requirement:
64-bit Linux/Unix/Ubuntu Operating Systems, python3 
•  Memory (RAM):
--Minimum: 1 GB (for basic script execution)
--Recommended: 2 GB or more (to comfortably run the script along with other applications)
•  Storage:
--Minimum: 100 MB (to install Python and any required libraries)
--Recommended: 1 GB or more (to store multiple projects and related files)


5.Theory:
•  Variables and Data Types:
--Balance: This variable stores the current balance of the bank account, initialized to 0.
--Transactions: This variable holds the list of transaction strings, split from the input.
•  Functions:
--Deposit: This function takes the current balance and an amount to deposit. It returns the new balance after adding the deposit amount.
--Withdraw: This function takes the current balance and an amount to withdraw. It checks if the balance is sufficient for the withdrawal and returns the new balance if the withdrawal is successful. If not, it returns the original balance and prints an error message.
•  Control Structures:
--if-else statements: Used to determine whether a transaction is a deposit or withdrawal, and to handle invalid transaction types.
--for loop: Iterates through each transaction in the input list to process them sequentially.
•  String Manipulation:
--split: Used to divide the input string into individual transactions and further split each transaction into its action and amount components.
•  Input and Output:
--Input: Reads a single line of input from the user.
--Print: Outputs the final balance to the user.

6.Algorithm:
• Deposit (amount, balance):
1.Enter the amount to be deposited
2.Add entered amount in current balance
3.Display updated balance
• Withdrawal (amount, balance):
1.Enter the amount to be withdrawn
2.Check if entered amount is greater than balance then display message insufficient balance
3.Else subtract entered amount from current balance
4.Display Updated Balance

8.Conclusion:
To Understand the concept of list and function. The program successfully handles a series of deposits and withdrawals, accurately computing the net balance while ensuring withdrawals do not result in a negative balance. This exercise illustrates the importance of structured programming and error handling in creating robust and reliable applications.
