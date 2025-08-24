s='ababab'
#every character has their own index ----->0,1,2,3,4,.....n.
                                #    ----->-6,-5,-4,-3,-2,-1..........n.
#how to get a character from index


#subscript operator
#syntax ----> prefix[index]
# ch=s[1]
# print(ch)
# print(s[1])
# print(type(ch))
# print(s[-5])
# print("python"[-1])
# print(s[10]) error (out of index)
# print(s[-9]) error (out of index)

#how to get index from a character
#syntax
'''--> str.index(char)
   --> str.index(char,start)
   --> str.rindex(char)
   --> str.find(char)
   --> str.find(char,start)
   --> str.rfind(char)
'''
print(s.index('b'))#returns pos index of first occurnce only, error if not present.

print(s.index("b",2))#index (char,startposition)--->will start searching from given startposition
print(s.index("b",-4))#index (char,startposition)--->will start searching from given startposition
print(s.rindex("b"))#return pos index of last occurence
print(s.find("b"))#returns positive index first occurence...,-1 if not present.
print(s.find("B"))
print(s.rfind("b"))
