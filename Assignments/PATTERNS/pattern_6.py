'''
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
'''
print("")
for i in range(6,0,-1):
    # for k in range(5):
    #     d=20
    for j in range(1,i):
        print(i-j,end=" ")
        # k-=1
    print(" ")
