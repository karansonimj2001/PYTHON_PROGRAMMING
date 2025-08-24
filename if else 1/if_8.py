option=input("""Select an option
1. Even/Odd
2. Neg/Pos
""")

match option:
    case "1":
        num=int(input("enter num="))
        if num%2==0:print("even")
        else:print("odd")
    case "2":
        num=float(input("enter num="))
        if num>=0:print("pos")
        else:print("neg")
    case _:
        print("invalid option")

