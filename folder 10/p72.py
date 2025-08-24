#match case condition (added in 3.10 version)

option="2"
match option:
    case "1"|"2":
        print("apple")
    case "2"|"3":
        print("mango")
    case _:#default
        print("invalid option")


#write the above code using if condition
if option=="1" or option=="2":
    print("apple")
elif option=="2" or option=="3":
    print("mango")
else:
    print("invalid option")

print("thank you")
