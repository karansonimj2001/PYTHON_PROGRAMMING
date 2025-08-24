#Nested loop
for i in range(1,5):   #outer/top level loop
    print('hi')
    while i<3:         #nested/inner loop
        print('hello')
        i+=1
    print('bye')

print("-------------")
for i in range(1,5):   #outer/top level loop
    print('hi')
    while i<3:         #nested/inner loop
        print('hello')
        i+=1
        break
    print('bye')
print("----------")
for i in range(1,5):   #outer/top level loop
    print('hi')
    while i<3:         #nested/inner loop
        print('hello')
        i+=1
    break
    print('bye')
