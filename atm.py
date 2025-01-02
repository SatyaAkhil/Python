
print("*** HDFC BANK ***")
Entercard=input("enter card number: ")
Enterpin=input("enter pin:")
if Entercard=="123456789" and Enterpin== "1122":
    print("Hello John!")
else:
    print("Wrong card or pin")   
    exit()     
balance = 0
i=1
while i<=3:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit")
    i=i+1
    choice= input("Enter your choice: ")
    if choice=="1":
        amount=int(input("Enter amount : "))
        balance= balance+amount
        print("Current Balance is ",amount)
    elif choice=="2":
        amount=int(input("Enter Amount: "))
        if balance<amount:
            print("insufficient Balance")
        else:
            balance=balance-amount
        print("current balance is:",balance)
    elif choice=="3":
        print("Transaction Completed")
    else:
        break      
else: 
    print("program is completed")