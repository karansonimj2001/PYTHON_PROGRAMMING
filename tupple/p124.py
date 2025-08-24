#Creating tuple with one value
t=(10)
print(t,type(t))

t=(10,)
print(t,type(t))

x=[10]
print(x,type(x))

x=[10,]
print(x,type(x))

#creating tuple without ()
t=10,20,30
print(t,type(t))

#creating tuple by joining 2 or more tuples
a=(10,20)
b=(20,30,40)
c=a+b
print(c)

#creating tuple by repeating an existing tuple n times
a=(10,20)
b=a*3
print(b)

#creating tuple using tuple()
t=tuple()            #empty tuple
print(t)

t=tuple("bharat")    #str to tuple
print(t)

t=tuple(range(1,11)) #range to tuple
print(t)

t2=tuple(t)          #copy of existing tuple
print(t2)

t=tuple([1,2,3,4,5]) #list to tuple
print(t)


