while True:
    a=int(input("enter a="))
    b=int(input("enter b="))
    print("Mul=",a*b)
    ch=input("do you want to run it again(y/n)?")
    if ch=='y':
        continue
    elif ch=='n':
        break
