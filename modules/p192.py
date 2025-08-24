import itertools
x=[0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','A','B','C','D','E','_','@','$']
prods=itertools.product(x,repeat=8)
for i in prods:
    print(i)
