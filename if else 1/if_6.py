p=float(input("enter marks in P="))
c=float(input("enter marks in C="))
m=float(input("enter marks in M="))

if m>=60 and p>=50 and c>=40:
    print("adm done")
elif (p+c+m)>=200:
    print("adm done")
elif (p+m)>=150:
    print("adm done")
else:
    print("adm not possible")

print("------------------")
if (m>=60 and p>=50 and c>=40) or ((p+c+m)>=200) or ((p+m)>=150):
    print("adm done")
else:
    print("adm not possible")
