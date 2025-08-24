#frozenset
#it is immutable version of set
#syntax
    #var=frozenset()
    #var=frozenset(iterable)

fs=frozenset() #empty
print(fs)

fs=frozenset(range(1,5))
print(fs)

for i in fs:
    print(i)

#fs.remove(2) #error:frozenset does not support remove
