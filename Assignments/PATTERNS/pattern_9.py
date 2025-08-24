'''
         1
        1 2 1
      1 2 3 2 1
    1 2 3 4 3 2 1
  1 2 3 4 5 4 3 2 1
    1 2 3 4 3 2 1
      1 2 3 2 1
        1 2 1
          1
'''

for i in range(1,6):
    for j in range(i,6):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(k,end=" ")
    for l in range(k-1,0,-1):
        print(l,end=" ")
    print(" ")


for a in range(1,5):
    for b in range(a,-1,-1):
        print(" ",end=" ")
    for c in range(b+1,6-a):
        print(c,end=" ")
        
    for d in range(c-1,0,-1):
        print(d,end=" ")
        
    print(" ")

