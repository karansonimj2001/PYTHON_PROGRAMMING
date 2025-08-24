#var=[expression for for ....for]
x=[i*j for i in range(1,3) for j in range(2,4)]
print(x)

x=[i+j+k for i in range(1,3) for j in range(2,4) for k in range(4)]
print(x)

#without comprehension
x=[]
for i in range(1,3):
    for j in range(2,4):
        for k in range(4):
            x.append(i+j+k)
print(x)

#var=[true_exp if condition else false_exp for]
x=[i*i if i%2==0 else i+i for i in range(2,10)]
print(x)

#creating list using comprehension by user input
x=[int(input('enter value=')) for i in range(3)]
print(x)

#creating list by converting each char of string in upper
x=[i.upper() for i in "python"]
print(x)

#creating list by taking sqr of elements of an existing list
x=[1,2,3,4,5]
y=[i**2 for i in x]
print(x)
print(y)



