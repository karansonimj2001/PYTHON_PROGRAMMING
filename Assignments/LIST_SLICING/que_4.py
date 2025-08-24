#write a python program to remove duplicates from a list.

list1=[1,23,3,23]

list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)

print(list2)
