print("----find greatest of three numbers----")
num1=int(input("enter the 1 number here : "))
num2=int(input("enter the 2 number here : "))
num3=int(input("enter the 3 number here : "))
if num1>num2:
    if num1>num3:
        print(num1,"is the greatest of all")
elif num2> num3:
    print(num2,"is the greatest of all")
else:
    print(num3,"is the greatest of all")