m1=int(input("enter marks in 1st subject="))
m2=int(input("enter marks in 2nd subject="))
m3=int(input("enter marks in 3rd subject="))
m4=int(input("enter marks in 4th subject="))
m5=int(input("enter marks in 5th subject="))

if m1>=40 and m2>=40 and m3>=40 and m4>=40 and m5>=40:

    avg=(m1+m2+m3+m4+m5)/5

    if avg>=40 and avg<50:
        print("3rd div")
    elif avg>=50 and avg<60:
        print("2nd div")
    elif avg>=60:
        print("1st div")
else:
    print("Fail")
