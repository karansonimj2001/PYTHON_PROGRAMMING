a=0
b=1
print(a,end=" ")
print(b,end=" ")
c=0
while True:
    c=a+b
    if c<=50: 
        print(c,end=" ")
        a=b
        b=c
    else:
        break
