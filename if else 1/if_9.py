option=input("""Select an option
1. Add
2. Sub
3. Mul
4. Div
5. Inverse
6. Sqr
7. Cube
""")

match option:
    case "1":
        a=int(input("enter a="))
        b=int(input("enter b="))
        print(a+b)
    case "2":
        pass
    case "3":
        pass
    case "4":
        pass
    case "5":
        num=int(input("enter num="))
        print(num**-1)
    case "6":
        pass
    case "7":
        pass
    case _:
        print("invalid option")

