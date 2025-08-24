#wrtie a python program to get a char in a string just before specified substring.
str="hello*world"
sub_str="world"
a=str.find(sub_str)
k=a-1
find=str[k]

print(k)
print(find)