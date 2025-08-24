#create an empty set
#add 5 int values from user
#find length,min,max,sum
#print values of set in asc order

s=set()
for i in range(5):
    v=int(input("enter value="))
    s.add(v)
print(len(s))
print(min(s))
print(max(s))
print(sum(s))
print(sorted(s))
