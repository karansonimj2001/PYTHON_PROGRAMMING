#write a function that takes numbers entered through keyboard and return the sum of digits of entered numbers.
# num2=int(input("enter the number here :"))
def add_num(num1):
    list1=[]
    for i in num1:
        # num1=int(num1)
        list1.append(int(i))
        
    print(list1)
    return sum(list1)
# num=add_num(num1,num2)
num=input("enter the number here :")

print("sum =",add_num(num))
