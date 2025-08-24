#write a function to print the entered number in reverse order.
def revrs(num):
    list1=[]
    list2=[]
    num=str(num)
    for i in num:
        list1.append(i)
    list1.reverse()
    # print(list1)
    result=""
    for j in list1:
        result=result+j
    return result    
    # num.reverse()
    # print(num)
num2=int(input("enter the number here : "))
# num2=[1,2,3,4,5,6,7,8,9,10]
# print(num2)

print("this is the number in reversed :",revrs(num2))

