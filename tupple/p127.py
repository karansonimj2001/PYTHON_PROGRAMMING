t=(10,20,[1,2,3])
print(t)

x=t[-1]
print(x)
x.append(4)
print(x)
print(t)

t[-1].append(100)
print(t)
print(t[-1][0])
