#WAP to print all even and odd numbers between 1 and 100.
start=int(input("enter the starting number here : "))
stop=int(input("enter the stop number here : "))
for i in range(start,stop+1):
    if i%2==0:
        print(i,"is even")
    else:
        print(i,"is odd")