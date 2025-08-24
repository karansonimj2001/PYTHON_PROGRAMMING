#break keyword
    #it is used to suspend current as well as all next iterations.
    #i.e. it terminates the loop explicitly.
    #it can only be used inside loop.
x=1
while x<=5:
    print(x)
    x+=1
    if x==2 or x==5:
        break
    print("hi")

