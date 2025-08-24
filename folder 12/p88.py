bal=int(input("enter initial bal="))
while True:
    option=input("""Select an option
    d. deposit
    c. check bal
    w. withdraw
    """)

    match option:
        case 'd':
            amt=int(input("enter amout="))
            bal+=amt
            print("Updated Bal=",bal)
        case 'c':
            print("Available Bal=",bal)
        case 'w':
            if bal>=500:
                amt=int(input("enter amout="))
                if bal>=amt:
                    bal-=amt
                    print("Updated Bal=",bal)
                else:
                    print("insufficient bal")
            else:
                print("you can not withdraw as min bal is below 500")
        case _:
            print("invalid option")
    choice=input("do you want to run it agian(y/n)?")
    if choice=='y':
        continue
    if choice=='n':
        break
print("thank you")
