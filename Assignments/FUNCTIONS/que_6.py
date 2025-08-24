#write the function to find entered number through keyboard is whether armstrong or not .
def armstrong(num1:int):
    num=str(num1)
    x=[]
    for i in num:
        num=int(i)**3
        # print(num)
        x.append(num)
    total=sum(x)
    # print("-----")
    print(num1)
    if num1==total:
        return 'it is a armstrong number'
    else:
        return 'it is not an armstrong number '
num=int(input("enter the number here : "))
a=armstrong(num)
print(a)