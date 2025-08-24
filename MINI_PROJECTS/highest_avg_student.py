p=[45,56,78,90]
c=[66,77,34,67]
m=[80,78,89,67]
num1=1
num2=0
avg=[]
list1=[]
list2=[]
for i in zip(p,c,m):
    
    print("report card of the ",num1,"student")
    print("physicis  : ",p[num2])
    print("chemistry : ",c[num2])
    print("maths     : ",m[num2])
    total=round(sum(i)/3,2)

    
    print("average marks are : ",total)#will add the average in the list
    avg.append(total)#will add the average in the list(avg)


    list2.append(num1)
    list2.append(total)
    list1.append(list2)
    num1=num1+1
    num2=num2+1



max1=max(avg)
print("m",max1)

print(list2)
index1=list2.index(max1)
print(index1)
print("this is the highest average : ",max1,"scored by the student ",list2[index1-1])