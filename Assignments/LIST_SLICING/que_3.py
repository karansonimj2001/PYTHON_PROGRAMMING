#write a python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
list1=['abc','xyz','aba','1221','a']
print(list1)
num=0
for i in list1:
    if len(i) > 1 and i[0] == i[-1]:
        num+=1
print(num)