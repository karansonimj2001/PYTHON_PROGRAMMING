a=int(input("enter a="))
b=int(input("enter b="))
c=int(input("enter c="))

if a>b and a>c:
    print("a>b,c")
elif b>a and b>c:
    print("b>a,c")
elif c>a and c>b:
    print("c>a,b")
elif a==b and a>c:
    print("a,b>c")
elif a==c and a>b:
    print("a,c>b")
elif b==c and b>a:
    print("b,c>a")
elif a==b and a==c:
    print("a=b=c")
