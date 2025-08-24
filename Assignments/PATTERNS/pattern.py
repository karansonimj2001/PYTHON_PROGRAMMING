for i in range(1,6):
    for j in range(0,i):
        print(i,end=" ")
    print(" ")

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print(" ")

num=1
for i in range(1,7):
    for j in range(1,i):
        print(num,end=" ")
        num+=1
    print(" ")


for i in range(0,6):
    for j in range(i,0,-1):
        print(j,end=" ")
    print(" ")

print(" ")
for row in range(5,0,-1):
    for coloumn in range(1,row):
        print(" ",end=" ")
    for m in range(6,0,-1):
        k=20
    for space in range(5,row,-1):
        print(m,end=" ")
        m+=1
    print(" ") 

print("")
for i in range(6,0,-1):
    # for k in range(5):
    #     d=20
    for j in range(1,i):
        print(i-j,end=" ")
        # k-=1
    print(" ")
print("-----------------------")

# print("")
num=5
for i in range(1,6):
    for j in range(i,0,-1):
        print(" ",end=" ")
    for m in range(6,0,-1):
        d=21
    for k in range(6,i,-1):
        print(m,end=" ")
        m=m+1
    print(" ")
print("-----------------------")

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
print(" ")
for i in range(1,6):
    for j in range(i,6):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(k,end=" ")
    for l in range(k-1,0,-1):
        print(l,end=" ")
    print(" ")


for a in range(1,6):
    for b in range(a,-1,-1):
        print(" ",end=" ")
    for c in range(1,c):
        print(c,end=" ")
        
    for d in range(c-1,0,-1):
        print(d,end=" ")
        
    print(" ")


print("---------------------")

for i in range(1,7):
    for j in range(1,i):
        print(i-j,end=" ")
    print(" ")
print(" ")

for i in range(1,6):
    for j in range(6,i,-1):
        print(i,end=" ")
        i=i+1
    print(" ")