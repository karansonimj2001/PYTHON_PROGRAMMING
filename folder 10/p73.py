a=int(input("enter n1="))
b=int(input("enter n2="))
choice=input("""Select your option
1. Add
2. Mul
3. Sub
""")

match choice:
    case "1":
        print("add=",a+b)
    case "2":
        print("mul=",a*b)
    case "3":
        print("sub=",a-b)
    case _:
        print("invalid option")

