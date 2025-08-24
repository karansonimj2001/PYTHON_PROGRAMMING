#Removing values from list
x=[1,2,1,3,4,1,5,6,1,7,1]
print(x)

#1. by index using del operator
#syntax-->del list[index]
del x[1]  #remove element from given index,error if out of range
print(x)

#2.1 by index using pop() method
#syntax-->value=list.pop(index)
val=x.pop(1)
print(x,val)

#2.2 value=list.pop() #default index=-1
val=x.pop()
print(x,val)
#3. by value using remove() method
#syntax-->list.remove(value)
x.remove(1) #remove only first occurrence,error if not present
print(x)

#4.1 removing all occurrences of a value
c=x.count(1)
print(c)
for i in range(c):
    x.remove(1)
print(x)

#4.2 removing all occurrences of a value
x=[2,1,4,1,5,1,6,1]
#print(1 in x)
while 1 in x:
    x.remove(1)
print(x)

#5. removing all values from list
x.clear()
print(x)




