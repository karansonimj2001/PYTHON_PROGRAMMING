#if elif elif .....else
avg=float(input("enter avg marks="))
if avg<30:
    print("fail")
elif avg>=30 and avg<=44:
    print("3rd div")
elif avg>=45 and avg<=59:
    print("2nd div")
elif avg>=60 and avg<=100:
    print("1st div")
else:
    print("invalid marks")
print("thank you")
