#read a str from user and also a char to searched anywhere
#read another char to replace with previously entered char
    #o/p
        #enter string=python
        #enter a char=t
        #t is present in python
            #enter another char=a
            #replaced string=pyahon

s=input("enter string=")
ch=input("enter char=")

if ch in s:
    print(f"{ch} is present in {s}")
    ch2=input("enter another char=")
    print(f"replaced string={s.replace(ch,ch2)}")
else:
    print(f"{ch} is not present in {s}")
    
