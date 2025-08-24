#create empty list
#read 3 int values from user
#append them to list
#find min,max,sum

a=int(input("enter value="))
b=int(input("enter value="))
c=int(input("enter value="))
x=[a,b,c]

print(".........")
x=[]
a=int(input("enter value="))
b=int(input("enter value="))
c=int(input("enter value="))
x.extend([a,b,c])

print(".........")
x=[]
for i in range(3):
    a=int(input("enter value="))
    x.append(a)    
print(x)
