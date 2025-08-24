#write a python program to sort a string lexicographically(ascending).
string=input("enter the string here : ")
string=string[0::]
print("this string is in unodered form : ",string)
num=0
list1=[]
for i in string:
    string1=string[num:num+1:1]
    num=num+1
    add_list=list1.append(string1)
    # print(string1)
    list1.sort()
# print(list1)
concatenate_list=str(list1)
print("this string is now in ascending order : ")
for i in list1:
    print(i,end="")