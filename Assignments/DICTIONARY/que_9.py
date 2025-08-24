#Write a Python program to remove duplicates(based on values) from Dictionary.

dict1={1:'rahul',2:'karan',3:'shohaib',4:'karan',5:'varun'}
print(dict1)

dict2={}
for k,v in dict1.items():
    if v not in dict2.values():
        dict2[k]=v
print(dict2)