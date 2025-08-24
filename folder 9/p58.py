#profit/loss using cost & selling price
#input marks of 3 subject,avg marks above or equal 60,adms
#gst rate
    #product food---->5%
    #other product--->10%

cp=float(input("enter cp="))
sp=float(input("enter sp="))
if sp>cp:
    print("profit")
else:
    print("loss")

print("--------------")
m1=int(input("enter m1="))
m2=int(input("enter m2="))
m3=int(input("enter m3="))
avg=(m1+m2+m3)/3
if avg>=60:
    print("adm")
else:
    print("adm not possible")


print("--------------")
p=input("enter product=")
if p=="food":
    print("5%")
else:
    print("10%")















