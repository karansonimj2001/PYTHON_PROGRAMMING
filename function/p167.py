def mul(a,b):
    if type(a)==int and type(b)==int:
        print(a*b)
    else:
        print("value are not compatiable")

mul(3,4)
mul(3.5,5.3)
mul('a','b')

#define a function to calculate area of circle
def area(r):
    print(3.14*r**2)

area(3)
#define a function to check even/odd of a num
def check(num):
    if num%2==0:
        print("even")
    else:
        print("odd")

#define a function to calculate avg marks of 3 subjects
def avg(a,b,c):
    a=(a+b+c)/3
    print(round(a,2))
avg(70,70,89)
#define a function to convert years into days
def conv(years):
    print(years*365)

conv(3)






    
