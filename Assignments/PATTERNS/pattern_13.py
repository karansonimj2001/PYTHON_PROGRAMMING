''' 
5 4 3 2 1  
  5 4 3 2
    5 4 3
      5 4
        5
'''
for a in range(1,6):
    for b in range(1,a):
        print(" ",end=" ")
    for c in range(5,a-1,-1):
        print(c,end=" ")
    print(" ")