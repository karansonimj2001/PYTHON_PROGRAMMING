#write a for loop to print counting in forward direction from
# a to b (both inclusive) with gap c
#input a,b,c from user

a=int(input("enter start="))
b=int(input("enter stop="))
c=int(input("enter gap="))

for i in range(a,b+1,c):
    print(i)
