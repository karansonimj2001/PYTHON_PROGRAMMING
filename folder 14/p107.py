s="ababab"
print(s)
for i in s:
    print(i)
print("-------")

#how to get a char from index

#subscript operator
#syntax-->prefix[index]

ch=s[1]
print(ch,type(ch))
print(s[-5])
print("python"[-1])
#print(s[10]) #error (out of index)
#print(s[-9])  #error (out of index)

#how to get index from a char
#syntax--
    #>str.index(char)
    #>str.index(char,start)
    #>str.rindex(char)
    #>str.find(char)
    #>str.find(char,start)
    #>str.rfind(char)

print(s.index('b'))  #returns pos index of first occurrence only,error if not present
print(s.index('b',2))#index(char,startPos)-->will start searching from given startPos
print(s.rindex('b')) #returns pos index of last occurrence
print(s.find('b')) #returns pos index of first occ..,-1 if not present
print(s.find('B'))
print(s.rfind('b'))















