import random
#random_int=random.randint(low,high)
print(random.randint(1000,9999))

#random_float=random.uniform(low,high)
print(random.uniform(1000,9999))

x=[10,20,30,40,50]
print(x)

#None=random.shuffle(list)#unorder the list values
random.shuffle(x)
print(x)

#random_value=random.choice(seq)
print(random.choice(x))
