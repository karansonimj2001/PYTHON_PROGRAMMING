s1={10,20,30}
s2={30,40,50}

#s3=s1+s2 #error

#Union:combine elements from both sets 
#1.
s3=s1.union(s2)
print(s3)

#2.
s3=s1|s2  #bitwise or
print(s3)

#Intersection:filter common elements in both sets
print(s1.intersection(s2))
print(s1&s2) #bitwise and

#Difference:remove common elements from 1st set
print(s1.difference(s2))
print(s1-s2)
print(s2-s1)

#Symmetric Difference:join uncommon elements from both sets
print(s1.symmetric_difference(s2))
print(s1^s2)  #bitwise xor



