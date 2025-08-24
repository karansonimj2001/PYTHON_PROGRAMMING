#create 2 empty lists
#input 3 values in both lists
#create 3rd list by joining
#read an int to repeat joined list

x=[]
y=[]

for i in range(1,4):
    v=int(input(f"enter {i} value in 1st list="))
    x.append(v)
print(x)

for i in range(1,4):
    v=int(input(f"enter {i} value in 2nd list="))
    y.append(v)
print(y)

z=x+y
print(f"Joined list={z}")
r=int(input("enter an int to repeat joined list="))
print(z*r)
