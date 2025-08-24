#Set
#>it is an unique collection of values
#>it does not maintain order of values
#>it is not subscriptable(does not support indexing & slicing)
#>it is iterable
#>it is mutable
#>it supports operations of set theory of maths

#Syntax
#var={v1,v2,v3,.....} #must contain atleast 1 value
#var=set()  #empty set
s={10,20,10,30,-5,0,100,'hi',False}
print(type(s))
print(s)
#print(s[0]) #error
for i in s:
    print(i)

s.add(50) #will add 50 at arbitrary position
print(s)

s.remove(10) #will remove only occurrence,error if not present
print(s)

s.clear()    #will remove all values
print(s)











