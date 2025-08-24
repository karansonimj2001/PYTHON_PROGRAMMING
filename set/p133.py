s1={10,20,30,40,50}
s2={20,40}
s3={20,50,60}
print(s2.issubset(s1)) #True,if s2 is having all elements of s1,else False
print(s3.issubset(s1))
print(s1.issuperset(s2))#True if s1 is having all elemets of s2
print(s1.issuperset(s3))

