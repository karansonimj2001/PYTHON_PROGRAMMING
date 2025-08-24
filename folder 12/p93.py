#write a for loop to print counting in forward direction from
# a to b 
#input a,b

a=int(input("enter start="))
b=int(input("enter stop="))

for i in range(a,b):
    if i%2==0:
        print(i,"is even")
    else:
        print(i,"is odd")
