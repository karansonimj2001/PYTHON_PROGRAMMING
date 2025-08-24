'''
          5
        5 4 5
      5 4 3 4 5
    5 4 3 2 3 4 5
  5 4 3 2 1 2 3 4 5
    5 4 3 2 3 4 5
      5 4 3 4 5
        5 4 5
          5
'''
print(" ")
for i in range(1,6):
    for j in range(6,i,-1):
        print(" ",end=" ")
    for k in range(5,6-i,-1):
        print(k,end=" ")
    for l in range(6-i,6,1):
        print(l,end=" ")
    print(" ")

for a in range(1,6):
    for b in range(-1,a):
        print(" ",end=" ")
    for c in range(5,a,-1):
        print(c,end=" ")
    for d in range(a+2,6):
        print(d,end=" ")
        
    print(" ")
