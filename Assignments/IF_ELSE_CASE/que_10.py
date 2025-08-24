var1=input("""press w for withdraw
press d for deposit
press c for checking balance 
ENTER THE VALUE HERE : """)
minimum_balance=500
match var1:
    case "W" | "w":
        withdraw=float(input("enter the amount you want to withdraw :"))
        if minimum_balance<=withdraw:
            print("withdraw amount shoud be greater then or equal to the minimum balance ")
        else:
                print("withdraw of ",withdraw,"successful.")
    case "D" | "d":
        deposit=float(input("enter the amount you want to deposit :"))
        print("deposit of ",deposit,"successful")

    case "C" | "c":
        print("current balance : ",minimum_balance)
    case _:
          print("invalid choice. please enter (w,W)/(d,D)/(c,C)")

print("THANK YOU")