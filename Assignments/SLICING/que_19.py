#write a python program to move spaces to the front of a given string.

string1="hello , this is a string"
print(string1)
count=string1.count(" ")
string1=string1.replace(" ","")
# print(count)
print(" "*count,string1)
# print(i)
# print(count)