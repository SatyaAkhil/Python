print("***HDFC BANK***")
balance=0
while True:
    print("1.Create Account")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    choice=input("Enter your Choice: ")
    if choice=="1":
        details=[]
        for i in range(1):
            detail={}
            Username=input("enter Name: ")
            Accountno=input("Enter Accnumber:")
            pin=input("Enter pin:")
            InitialBal=input("Enter Bal:")
            detail={"Username":Username,"Accountno":Accountno,"pin":pin,"InitialBal":InitialBal}
            details.append(detail)
        for i in details:
             print(f'{i["Username"]}-{i["Accountno"]}-{i["pin"]}-{i["InitialBal"]}')    
             print("Account is created")
             

    elif choice=="2":
        amount=int(input("Enter Amount: "))
        balance=balance+amount
        print("Total Balance is:",balance)
    elif choice=="3":
        amount=int(input("Enter Amount: "))
        if balance<amount:
            print("Insufficient Balance")
        else:
            balance=balance-amount
            print("Total Balance is: ",balance) 
    elif choice=="4":
        print("Transaction completed")
        break
    else:
        break
else:
    print("program is completed")               
