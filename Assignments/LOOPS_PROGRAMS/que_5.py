#WAP to print calculate the factorial of number entered through keyboard.
num=int(input("ente the number here : "))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
    print(factorial)
    