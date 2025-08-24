#write the function to print the fibonacci series. the number of items for fibonacci series will be entered thorugh keyboard.
def fibonacci(num2):
    num1=0
    num=1
    while num1<num2:
        print(num)
        num1,num=num,(num1+num)
    return num1
num_1=int(input("enter the number here : "))
fibonacci(num_1)
