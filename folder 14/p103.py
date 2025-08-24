s="india is india"
print(s)
#str.replace(old,new)#returns a new string after replacement with
#all occurrences
print(s.replace('i','I'))
print(s.replace('in','In'))

#str.replace(old,new,occurrences)
print(s.replace('i','I',2))

s="  virat kohli  "
print(s)
#str.strip():returns a new str after removing leading & trailing spaces
print(s.strip())

#str.lstrip():returns a new str after removing only leading spaces
print(s.lstrip())

#str.rstrip():returns a new str after removing only trailing spaces
print(s.rstrip())

#trick to replace all spaces
print(s.replace(" ",""))

