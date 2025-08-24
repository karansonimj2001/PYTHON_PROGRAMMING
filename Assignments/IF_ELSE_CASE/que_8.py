print("""select 1 to find out whether the number is even or odd 
select 2 to find out whether the number is negative or positive """)
var1=int(input("chose one of the option : "))
match var1:
    case 1:
        print("----find out whether the number is even or odd----")
        num=float(input("enter the number here : "))
        if num%2==0:
            print(num,"is an even number")
        else:
            print(num,"is an odd number")
    case 2:
        print("----find out whether the number is positive or negative----")
        num1=float(input("enter the number here : "))
        if num1<0:
            print("the number is negative")
        else:
            print("the number is positive")