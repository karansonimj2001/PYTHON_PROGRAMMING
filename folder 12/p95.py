"""
2 4 6   8
3 6 9  12   
4 8 12 16
..
.
"""

for i in range(2,8):#2,3,4
    for j in range(1,6):
        print(i*j,end="\t")
    print()

print("===================================")
"""
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""
for i in range(6,1,-1):#6,5,4,3,2
    for j in range(1,i):
        print(j,end=" ")
    print()

print("===================================")
"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
for i in range(2,7,1):
    for j in range(1,i):
        print(j,end=" ")
    print()

print("===================================")
"""
1
2 3
4 5 6
7 8 9 10
"""
x=1
for i in range(2,6):
    for j in range(1,i):
        print(x,end=" ")
        x+=1
    print()
print("=======================")

"""
        5
      5 4
    5 4 3
  5 4 3 2
5 4 3 2 1
"""

for i in range(5,0,-1):
    for j in range(1,i):
        print(" ",end=" ")
    for k in range(5,i-1,-1):
        print(k,end=" ")
    print()
    










