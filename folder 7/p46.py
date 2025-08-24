#wap to find simple interest,total amt
#logic-->i=p*r*t/100
#logic-->total=p+i

p=int(input("enter amt="))
r=float(input("enter roi="))
t=int(input("enter time="))
i=p*r*t/100
ta=p+i
print("Interest",i)
print("Total Amt",ta)


