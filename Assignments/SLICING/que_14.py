#write a python program to lowercase first n characters in a string.

string="THIS IS A STRING ."

ask=int(input("enter the value here : "))
string=string[:ask].lower()+string[ask:]
print(string)
