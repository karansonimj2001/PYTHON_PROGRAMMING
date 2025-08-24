#write a python program to check if a string contains all vowels of the alphabets.
string1="aeiouAEIOU"
# ask=input("enter the string here : ")
# for i in ask:
#     string2=string1.find(i)
#     # print(string2)
#     if string2==-1:
#         continue
#     else:
#         print("yes,",ask,"includes vowel : ",string1[string2])
#         break







list1=[]
for i in string1:
    value=ord(i)
    # print(i,ord(i))
    list1.append(value)
# print(list1)
ask=input("enter the string here : ")
for j in ask:
    value1=ord(j)
    # print(j,value1)
    if value1 in list1:
        print(j,":is a vowel ")
    else:
        # print(j,":not a vowel ")
        pass
        