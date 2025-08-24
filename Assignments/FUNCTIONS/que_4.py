#write the function to calculate the factorial of a entered number.
def factor(num:int)->int:
    factorial=1
    for i in range(1,num+1):
        factorial=factorial*i
    return factorial
num1=int(input("enter the number here : "))
print("the factorial of the entered number is",factor(num1))
