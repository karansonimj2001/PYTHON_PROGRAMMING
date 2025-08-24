#write a python script to generate and print a dictionary that contains a number (between 1 and n ) in the form (x,x*x)
#sample dictionary (n=5):
#expected output :{1:1,2:4,3:9,4:16,5:25}

dict1={}
ask=int(input("enter the number here : "))
for i in range(1,ask+1):
    # print(i,i*i)
    a=i*i
    dict1[i]=a
print(dict1)