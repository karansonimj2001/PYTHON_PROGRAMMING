#memory point of view
#A variable is a pointer/reference to memory block where value
#is stored.
x=10
print(id(10))
print(id(x))

#id(value):returns virtual address of value during execution
#id(var):returns virtual address of value refered by given variable

y=10
z=10
print(x,id(x))
print(y,id(y))
print(z,id(z))
x=20
print(x,id(x))
print(y,id(y))
print(z,id(z))
#Note:int/float/str/bool values are immutable and if we change these
#values then a new memory is allocated 
