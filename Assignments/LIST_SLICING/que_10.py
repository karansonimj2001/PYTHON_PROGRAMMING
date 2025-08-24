#write a python program to get unique values from a list.

list1=[10,20,30,40,50,60,70,80,90,100]
print(list1)
list2=[]
list1=set(list1)
# print(list1)
for i in list1:
    list2.append(i)
print(list2)