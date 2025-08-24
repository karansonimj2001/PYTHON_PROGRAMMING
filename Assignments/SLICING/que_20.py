# #wrtie a python program to capitalize first and last letter of a given string.
# string1="this is a string"
# print(string1)
# string1=string1.capitalize()
# print(string1)
# for i in string1:
#     if i ==string1[-1]:
#         i=i.capitalize()
#         print(i)
#         break
#     print(i,end="")

#QUESTION 21.
#write a program to remove duplicate characters of a given string.

# string1=input("enter the string here :")
# print(string1)
# string2=""
# for i in string1:
#     if i not in string2:
#         string2=string2+i
#     else:
#         pass
# print(string2)



#QUESTION 22.

#WAP to find of occurences of characters of entered through keyobard.if the caharaccter o is not present in the string then show a message " o is not present in the entering string"

# sol - 

# string=input("enter the string here : ")
# find=input("enter the alphabet you want to find : ")
# if find in string:
#     print("yes,",find,"is in the string.")
# else:
#     print(find,"is not in the given string.")



#QUESTION 23.
#WAP which read the string and print only vowels characters of entered string on computer screen.
# sol-

# string1=input("enter the string here : ")
# vowels="aeiouAEIOU"
# new_str=""
# for i in string1:
#     if i in vowels:
#         if i not in new_str:
#             new_str=new_str+i
# print(new_str,"is used in the given string .")



#QUESTION 24.
#WAP that reads a string form keyboard and determine whether the string is palindrome or not.
#sol -
string1=input("entet the letter here : ")
string2=""
for i in string1:
    string2=i+string2

if (string1==string2):
    print("it is a pelindrome.")
else:
    print("it is not a pelindrome.")