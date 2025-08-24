#write a function that takes a number entered through keyboard and find whether it is postive or negative.
def postive_negative(num1):
    if num1>=0:
        return "it is an postive number here "
    else:
        return "it is a negative number here "

num1=int(input("enter the number here : "))
num=postive_negative(num1)
print(num)