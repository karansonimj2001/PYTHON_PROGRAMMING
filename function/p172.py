def show(*a,b):
    print(a,b)

show(1,2,3,4,b=5)

def show(a,*b):
    print(a,b)

show(1,2,3,4,5)

def show(*a,**b):
    print(a,b)

show(1,2,3,4,5)
show(1,2,i=3,j=4)

#define a function to calculate area of circle using r as
#positional only parameter
def area(r,/):
    print(3.14*r**2)


#define a fun to calculate avg marks of n subjects using var length
#positional param

def avg(*m):
    print(sum(m)/len(m))

#define a fun to calculate simple interest using r as default arg
#with value 8.5,p as positional only,t as keyword only

def si(p,/,r=8.5,*,t):
    print(p*r*t/100)
    

area(4.5)
avg(20,30,40,50,60)
si(4000,t=4)







