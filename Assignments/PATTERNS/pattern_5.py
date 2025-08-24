'''
        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5
'''
print(" ")
for row in range(4,0,-1):
    for space in range(1,row):
        print(" ",end=" ")
    for m in range(6,0,-1):
        k=20#not in use 
    for  coloumn in range(5,row,-1):
        print(m,end=" ")
        m+=1
    print(" ") 
