num=int(input("enter the number here : "))
prime=True
for i in range(2,num):
    if (num%i==0 and num!=2):
        prime=False
        break
if prime:
        print("it is a prime number ")
else:
    print("it is not a prime number ")
    