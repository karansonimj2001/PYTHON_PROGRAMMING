#write a python program to print a specified list after removing the 0th ,4th and 5th elements.

# list1=[1,2,3,4,5,6,7]
list1=['red','green','white','black','pink','yellow']
list2=[]
for i in list1:
    if i ==list1[0]:
        continue
    if i== list1[4]:
        continue
    if i==list1[5]:
        continue
    else:
        list2.append(i)
print(list2)