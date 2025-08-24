#tuple
#>it is immutable/unmodifiable version of list
#>it takes less memory to store same values than list
#>more efficient to iterate same values than list

#syntax
#var=()
#var=(v1,v2,.....)
#var=tuple()
#etc.

t=()
print(t,type(t))

t=(10,20,30,5,6,10)
print(t)
print(t[-1])
for i in t:
    print(i)
print(len(t))
print(min(t))
print(max(t))
print(sum(t))
print(sorted(t)) #returns a list in asc order
print(sorted(t,reverse=True)) #returns a list in desc order
print(t)

#t[0]=100 #error:tuple does not support item assignment 
#del t[0] #error:tuple does not support item deletion
#t.append(100) #error:tuple does not append operation










