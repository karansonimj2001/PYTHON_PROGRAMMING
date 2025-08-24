cp=int(input("enter cp="))
sp=int(input("enter sp="))
if sp>cp:
    print("profit",sp-cp)
elif cp>sp:
    print("loss",sp-cp)
else:
    print("no profit no loss")

print("-------------------")
d=sp-cp
if d>0:
    print("profit",d)
elif d<0:
    print("loss",d)
else:
    print("no profit no loss")
