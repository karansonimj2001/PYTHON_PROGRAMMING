#String Formatting
#using var & expression in a string
a=int(input("enter a="))
b=int(input("enter b="))
msg="Multiply of a and b=a*b"
print(msg)

#1st -way using format specifiers
msg="Multiply of %d and %d=%.2f"%(a,b,a*b)
print(msg)

#2nd-way using positional parameters
msg="Multiply of {0} and {1}={2}".format(a,b,a*b)
print(msg)

msg="Multiply of {0} and {0}={0}".format(a,b,a*b)
print(msg)

msg="Multiply of {} and {}={}".format(a,b,a*b)
print(msg)

#3rd-way using keyword/name parameters
msg="Multiply of {i} and {j}={k}".format(j=b,k=a*b,i=a)
print(msg)

#4th-way using concatenation
msg="Multiply of "+str(a)+" and "+str(b)+"="+str(a*b)
print(msg)

#5th-way using f-string(added in 3.6)
msg=f"Multiply of {a} and {b}={a*b}"
print(msg)


