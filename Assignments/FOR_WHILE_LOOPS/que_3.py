#WAP to print sum of numbers from 1 and 100.
stop=int(input("enter the starting number here : "))
start=int(input("enter the stop number here : "))
x=0
for i in range(stop,start+1):
    x+=i
    print(x)
