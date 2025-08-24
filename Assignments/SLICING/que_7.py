#write a python program to convert a given string to all uppercase if it contains at leeast 2 uppercase characters in the first 4 characters.
string=input("enter the string here : ")
print(string)
string1=string[0:5]
turn=1
condition=True
while turn<=2:
    for i in string1:
        value=ord(i)
        if value>=65  and value<97:
            # print(turn)
            turn+=1
    else:
        break
if turn>=2:
    new_string=string.upper()
    print("this string contains two uppercase letters in the first 4 characters : \n",new_string)
else:
    print("this string does not contain any uppercase letter in the first 4 character : \n ",string)
