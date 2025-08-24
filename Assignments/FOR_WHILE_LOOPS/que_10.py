#write a program to count the total number of digits in a number.
num=int(input("enter the number here : "))
count=0
while num!=0:
    num=num//10
    print(num)
    count+=1
    print(count)