#write a function that takes two numbers a and b ,entered through keyboard and return the value of a power b.
a=int(input("enter the number here : "))
b=int(input("enter the number here : "))
def power_num(a,b):
    c=a**b
    return c
print(power_num(a,b))