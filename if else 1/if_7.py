option=input("""Select an option
1. Area of Rectangle
2. Area of Circle
""")

match option:
    case "1":
        l=float(input("enter L="))
        b=float(input("enter B="))
        print(l*b)
    case "2":
        r=float(input("enter R="))
        print(3.14*r**2)
    case _:
        print("invalid option")

