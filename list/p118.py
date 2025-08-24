#create 200 empty lists
#input 3 values in both lists
#create 3rd list by joining
#read an int to repeat joined list

y=[]
for j in range(1,3):
    x=[]
    for i in range(1,4):
        v=int(input(f"enter {i} value in {j} list="))
        x.append(v)
    y.append(x)

print(y[0])
print(y[1])
z=y[0]+y[1]
print(f"Joined list={z}")
r=int(input("enter an int to repeat joined list="))
print(z*r)
