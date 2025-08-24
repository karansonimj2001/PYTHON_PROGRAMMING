print("-----find if the given number is divisible by 3 or 5-----")

num1=int(input("enter the number here : "))
if num1%3==0 and num1%5==0:
    print("it is divisible by 3 and 5 both ")
elif num1%3==0:
    print("it is divisible by 3")
elif num1%5==0:
    print("it is divisible by 5")
else:
    print("it is not divisible by 3 or 5")