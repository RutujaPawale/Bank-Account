def balanceInquiry():
    global balance
    print("Your current balance is:",balance,"\n \n")
    repeat()

def cashDeposit():
    global balance
    dep_amt=int(input("Enter the amount you want to deposit:"))
    balance=balance+dep_amt
    print("Cash deposited successfully!! \n")
    balanceInquiry()
    repeat()
