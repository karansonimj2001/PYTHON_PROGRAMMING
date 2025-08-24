#Comparision/Relational Operators
#return boolean result(True/False)

print(10==3) #equal comparision
x=10
print(x==10)
print(10!=3) #not equal comparision
print(10>3)  #greater comparision
print(10>=0) #greater or equal comparision
print(10>=100)
print(10<3)  #less comparision
print(10<=10)#less or equal comparision

#Logical Operators
#operated on boolean values
#also return boolean values
#generally,we use logical operators to combine result of multiple
#comparisions.

#logical and (and keyword)
    # True and True --->True
    # True and False--->False
    # False and True--->False
    # False and False--->False


print(5>2 and 6<5)
print(True and False)
print(False and true) #correct
#print(True and true) #error

#logical or (or keyword)
    # True or True --->True
    # True or False--->True
    # False or True--->True
    # False or False--->False

print(5>2 or 6<5)
#print(False or true) #error
print(True or true)   #correct

#Note:logical operators(and/or) work smartly i.e. if decision can be made
#by just looking at 1st operand then 2nd operand is not executed.


#logical not(not keyword),(unary)

    #not True---->False
    #not False--->True

print(not 10>5)



    
    
