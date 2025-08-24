#input a string from user
#find length,min,max
#input an int from user then repeat the str according to int
#input another str from user then concat it with first string

a=input("enter string=")
print(len(a))
print(min(a))
print(max(a))
b=int(input("enter int="))
print(a*b)
c=input("enter another string=")
print(a+c)
print(a+' '+c)
