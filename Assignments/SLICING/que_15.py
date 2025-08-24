#write a python program to swap comma and dot in a string.
#exapmle : 32.054,23
#output : 32,054.23
ask=input("enter the string here  : ")
num=1
ask="`".join(ask.split(","))
ask=",".join(ask.split("."))
ask=".".join(ask.split("~"))
print(ask)