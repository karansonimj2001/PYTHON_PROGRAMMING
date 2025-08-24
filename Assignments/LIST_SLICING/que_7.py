#write a python program to print the numbers of a specified list after removing even numbers from it.
list1=[1,20,30,4,5,60,70,8,9,10,11,12,13,14,15]
list2=[]
for i in list1:
    if i%2!=0:
        list2.append(i)
print(list2)