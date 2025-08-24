x=[]
for i in range(3):
    a=int(input("enter value="))
    x.append(a)

t=tuple(x)
print(t)

x=list(t)
x.pop()
print(x)

t=tuple(x)
print(t)
