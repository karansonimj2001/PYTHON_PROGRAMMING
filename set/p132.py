s={10,20,30,40,50}
print(s)

s.remove(20) # remove given value,error if not present
print(s)

s.discard(10)#remove given value,does nothing if not present
print(s)

s.pop()      #remove an element from arbitrary pos
print(s)

s.clear()    #remove all elements
print(s)
