#match case condition (added in 3.10 version)

option=input("""select your language
1. english
2. hindi
""")
match option:
    case 1:
        print("english")
    case 2:
        print("hindi")
    case _:#default
        print("invalid option")
print("thank you")
