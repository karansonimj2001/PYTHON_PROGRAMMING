#write a function to find entered number thorugh keyboard is whether palindrome or not . 
# num=12325

# print(num1)
def palindrome(num1):
    num1=str(num1)
    num2=[]
    num3=[]
    for i in num1:
        num2.append(int(i))

    val=0
    for j in num2:
        val=val+1
        num3.append(num2[-val])
        i=1
    while i<=len(num2):
        if num2[i]==num3[i]:
            return "it is an palindrome "
            i+=len(num2)
        else:
            return "it is not an palindorme"
num=int(input("enter the number here : "))
newval=palindrome(num)
print(newval)
    # if Conndition==True:
    #     print("same")
    # else:
    #     print("not same")
# print(newval)
# for k in num3:
#     i=0
#     if k!=num3[i]:
#         print("same",k)
#         i=i+1
#     else:
#         print("not same",k)
# # for i in num2:
    
# print(num3)