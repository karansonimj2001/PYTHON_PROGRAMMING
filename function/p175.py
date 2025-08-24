def mul(a,b):
    c=a*b
    return c

def add(a,b):
    d=a+b
    return d

def div(a,b):
    e=a/b
    return e

a=mul(2,6)
b=add(1,2)
c=div(a,b)
print(c)

print(div(mul(2,6),add(1,2)))
