#write a python program to convert a list of characters into a string.
list1=[11,00,51," delhi "," greater noida "]
print(list1)
list2=[]
for i in list1:
    list2.append(str(i))
print(list2)
string=""
for j in list2:
    string=string+j
print(string)