#for-else
    #else block is only executed when for is terminated after
    #iterating all values of given iterable and if for is terminated
    #by break then else is not executed.

for i in range(3):
    print(i)
else:
    print("this is else")

print("---------")
for i in range(3):
    print(i)
    break
else:
    print("this is else")

print("---------")
for i in range(3):
    continue
    print(i)
else:
    print("this is else")
print("bye")
