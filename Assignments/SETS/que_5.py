#write a python program to remove an item from a set if it is present in the set.
set1=[2,1,3,4,5,6,7,9]
num=int(input("enter the number here : "))
if num in set1:
    set1.remove(num)
    print(set1)
else:
    print("this item is not in the list.")