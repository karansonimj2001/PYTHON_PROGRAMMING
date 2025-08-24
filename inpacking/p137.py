#Parallel iterations of multiple containers
#zip() function can be used to iterate multiple containers parellely
#it returns a tuple on each iteration and this tuple can be stored
#into a single loop var or unpacked into multiple vars
#Note:zip() iterates according to shortest length container
roll={1,2,3,4}
name=['a','b','c','d','a']
mark=(60,67,78,80,57)

for i in zip(roll,name,mark):#(1,'a',60),(2,'b',67),.....()
    print(i)

print("------------")

for i,j,k in zip(roll,name,mark):#(1,'a',60),(2,'b',67),.....()
    print(i,j,k)

#given the marks of 4 students in 3 subjects
p=[45,56,78,90]
c=[66,77,34,67]
m=[80,78,89,67]
r=[1,2,3,4]
avg_list=[]
#find avg marks for each student
for rl,ph,ch,mh in zip(r,p,c,m):
    avg=round((ph+ch+mh)/3,2)
    avg_list.append(avg)
    print(f'''********Report Card of Student - {rl}********
Ph={ph}
Ch={ch}
M={mh}
Avg={avg}
''')
print(f"Highest Avg Marks={max(avg_list)}")






