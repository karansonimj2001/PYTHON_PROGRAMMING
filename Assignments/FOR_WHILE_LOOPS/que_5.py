#WAP to print calculate the factorial of number entered through keyboard;
num=int(input('enter the number here : '))
factorial=1
if num<0:
    print("please enter a number which should not less then 0 .")
elif num==0:
    print("the factorial of the 0 is 1 .")
else:
    for i in range(1,num+1):
        factorial=factorial*i
        print(factorial)
    print("the factorial of ",num,"is : ",factorial)