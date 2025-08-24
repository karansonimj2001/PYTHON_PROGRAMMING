#creating empty list
x=[]
print(x,type(x))

x=list()
print(x)

#creating list with initial values
x=[10,20,25,10,3.5,'hi',True,[1,5]]
print(x)

#accessing a single value using index
print(x[0])

#replacing/updating an existing value using index
x[1]=50
print(x)

#iterate values using for
for i in x:
    print(i)
