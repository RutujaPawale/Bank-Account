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
