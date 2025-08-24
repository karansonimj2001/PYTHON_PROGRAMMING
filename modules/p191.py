import itertools
x=[1,2,3,4]
print(x)
print('-----combinations of 3 values----------')
combs=itertools.combinations(x,r=3)
for i in combs:
    print(i)
print('-------permutations of 3 values----------')
perms=itertools.permutations(x,r=3)
for i in perms:
    print(i)
print('-------catresian product of 3 values----------')
prods=itertools.product(x,repeat=3)
for i in prods:
    print(i)
