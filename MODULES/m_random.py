import random 
#
i=0
a1=[]
while i < 5:
    a=random.randint(1,10)
    a1.append(a)
    i=i+1
print(a1)

#

print(random.uniform(1000,9999))

#

a=[10,20,30,40,50,"karan","soni"]
random.shuffle(a)
print(a)

#

print(random.choice(a))

#

