#creating list using comprehension
#-->it is a technique that create a list in a single stmt using
#for loop and an expression.
#-->we may optionally using multiple for loops and if condition

#syntax
    #var=[expression for]
    #var=[expression for if]
    #var=[expression for for ....for]
    #var=[true_exp if condition else false_exp for]

#var=[expression for]
x=[i*i for i in range(1,4)]
print(x)

#without comprenhension
x=[]
for i in range(1,4):
    x.append(i*i)
print(x)

#var=[expression for if]
x=[i*i for i in range(1,5) if i%2==0]
print(x)

#without comprenhension
x=[]
for i in range(1,5):
    if i%2==0:
        x.append(i*i)
print(x)







