var1=float(input("""press 1 for addition
press 2 for subtraction
press 3 for multiplication
press 4 for devision
press 5 for the inverse of a number
press 6 for finding the square of a number
press 7 for finding the cube of a number
enter the selected value here :  """))
match var1:
    case 1:
        add1=float(input("enter the first number here : "))
        add2=float(input("enter the second number here : "))
        print("the sum of the two numbers are ",add1+add2)
    case 2:
        sub1=float(input("enter the first number here : "))
        sub2=float(input("enter the second number here : "))
        print("the subtraction of two numbers are ",sub1-sub2)
    case 3:
        mul1=float(input("enter the first number here : "))
        mul2=float(input("enter the second number here : "))
        print("the multiplication of the two numbers are ",mul1*mul2)
    case 4:
        division1=float(input("enter the first number here : "))
        division2=float(input("enter the second number here : "))
        print("the division of the two numbers are ",division1/division2)
    case 5:
        inv1=float(input("enter the number here  : "))
        print(inv1**-1)
    case 6:
        square1=float(input("enter the number here  : "))
        print("the square of the given number is :",square1**2)
    case 7:
        cube1=float(input("enter the number here  : "))
        print("the cube of the given number is :",cube1**3)