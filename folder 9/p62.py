num=int(input("enter num="))
if num%2==0 and num%3==0:
    print("divisible by both 2 and 3")
elif num%2==0:
    print("divisible by 2")
elif num%3==0:
    print("divisible by 3")
else:
    print("not divisible by both 2 and 3")
print("bye")
