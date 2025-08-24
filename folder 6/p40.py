#Type Conversion
    #-it is a process of converting one type value to other type
    #-a new copy is created for target type
    #2 types of conversion
        #Implicit--->by language
        #Explicit--->by programmer
#Why Type Conversion
    #- to perform operations on different compatiable values

print(4+5)
print(4.2+5.3)
print(4+5.3)   #implicit type conv(4(int) to 4.0(float))
print("hi"+"hello")
print("5"+"6")
#print("hi"+5)

#float to int(always explicit)
a=2.6
print(a)
b=int(a) #create a new copy for given value(float) in int type
print(b)
print(a)

#str to int(always explicit)
a="5"
b=int(a)#create a new copy for given value(str) in int type
print(b+1)
#print(a+1)

a="5k"
#b=int(a)#error


#int to float(implicit/explicit)
a=5
b=float(a)
print(b)

print(4+5.4)
print(float(4)+5.4)
print(4+int(5.4))

#str to float(always explicit)
a="2.5"
b=float(a)
print(b)

#bool to int(implicit/explicit)
x=True
print(int(x)+5) #explicit
print(x+5)      #implicit
print(False*True)

#int to bool(implicit/explicit)
a=10
b=bool(a)
print(b)

#int/float/bool/None to str (always explicit)
a=5
b=4.5
c=True

d=str(a)
print(d)
e=str(b)
print(e)
f=str(c)
print(f)
g=str(None)
print(g)



