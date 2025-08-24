#WAP a program to print sum of the following series 1power2 + 2power2 + 3power2 +....+10power2.
num=int(input("enter the start number here : "))
stop=int(input("enter the stop number here : "))
sum=0
for i in range(num,stop+1):
    sum+=i**2
print("the sum of the folowing series are",sum) 