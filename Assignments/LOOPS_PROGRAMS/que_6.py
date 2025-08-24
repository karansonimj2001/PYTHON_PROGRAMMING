#WAP to print the following triangle :
'''
    1
  2 3
4 5 6 
'''
num=1
for row in range(5,0,-1):
    for coloumn in range(1,row):
        print(" ",end=" ")
    for m in range(6,0,-1):
        k=20
    for space in range(5,row,-1):
        print(m,end=" ")
        m+=1
    print(" ") 