def mul(a,b):
    c=a*b

print(mul(3,3)) #None


def mul(a,b):
    c=a*b
    print(c)
    
print(mul(3,3)) #None

def calc(a,b):
    c=a+b
    d=a*b
    return c
    return d

print(calc(2,4))#6

def calc(a,b):
    c=a+b
    d=a*b
    return c,d  #tuple

print(calc(2,4))#(6,8)

def calc(a,b):
    c=a+b
    d=a*b
    return [c,d]  #list

print(calc(2,4))#[6,8]
