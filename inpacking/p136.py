#Unpacking of containers(list/tuple/set/frozenset)
#storing values of a container into separate valriables or a container
#if we want to unpack a container into a container then we use
#starred expression and it can be used only once.

#starred expr always represent a list no matter main container is
#list/tuple/set/frozenset

x=[10,20,30,40]
print(x)

a,b,c,d=x  #unpacking
print(a)
print(b)
print(c)
print(d)

    
x={10,20,30,40}
print(x)

a,b,c,d=x  #unpacking
print(a)
print(b)
print(c)
print(d)

x=[10,20,30,40]
#a,b,c=x         #error:too many values to unpack
#a,b,c,e,d=x     #error:not enough values to unpack

a,b,*c=x
print(a)
print(b)
print(c)

*a,b,c=x
print(a)
print(b)
print(c)

a,*b,c=x
print(a)
print(b)
print(c)

#*a,*b,c=x  #error

x={10,20,30,40}
a,*b,c=x
print(a)
print(b)
print(c)





















