#write a python program to count and display the vowels of a given text.
ask=input("enter the string here : ")
vowels="aeiouAEIOU"
ordvalue=0
Condition1=False
for i in ask:
    if i in vowels:
        a=ask.count(i)
        if i in vowels:
            print(i,"has occured ",a,"times in ",ask)

        else:
            continue
# if Condition==True:
# else:
#     pass