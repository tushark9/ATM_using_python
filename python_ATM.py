balance = 100000
while(True):
    print("     ATM     ")
    print("""
    1.     Balance
    2.    Withdraw
    3.     Deposit
    4.      exit
    """)

    try:
        option=int(input("Enter option :"))
    except Exception as e:
        print("Error",e)
        print("Enter only from 1,2,3 and 4")
        continue

    if option==1 :
        print("Balance $", balance)
    if option==2 :
        print("Balance $", balance)
        withdraw = float(input("Enter Withdreawl amount  $"))
        if withdraw>0:
            forwardbalance=(balance-withdraw)
            balance=forwardbalance
            print("Forwardbalance  $",forwardbalance)
        elif withdraw>balance:
            print("no funs in  account")
        else:
            print("none withdraw made")
    if option==3 :
        print("Balance $", balance)
        Deposit=  float(input("Enter Deposit amount  $"))
        if Deposit>0:
            forwardbalance=(balance+Deposit)
            balance=forwardbalance
            print("Forwardbalance  $",forwardbalance)
        else:
            print("none Deposit made")
    if option==4:
        exit()

