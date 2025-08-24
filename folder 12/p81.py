#continue keyword
    #it is used to suspend current iteration and start the next.
    #it can only be used inside loop
x=1
while x<=5:
    print(x)
    x+=1
    if x==2 or x==5:
        continue
    print("hi")

