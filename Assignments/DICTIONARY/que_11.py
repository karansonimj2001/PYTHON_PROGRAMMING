#write a python program to combine two dictionary adding values for common keys.
d1={"a":100,"b":200,"c":300}
d2={"a":300,"b":200,"d":400}
d3={}
for i in d1:
    if i in d2:
        d3[i]=d1[i]+d2[i]
    else:
        d3[i]=d1[i]
for j in d2:
    if j not in d3:
        d3[j]=d2[j]
print(d3)