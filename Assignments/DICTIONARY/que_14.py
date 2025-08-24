'''Write a Python program to match key values in two dictionaries.
Sample dictionary:{'key1':1,'key2':3,'key3':2}{'key1':1,'key2':2}
Expected output: key1: 1 is present in both x and y'''
d1={'key1':1,'key2':3,'key3':2}
d2={'key1':1,'key2':2}
t1=d1.items()
t2=d2.items()

for i,j in zip(t1,t2):
    if i[0]==j[0] and i[1]==j[1]:
        print(i)

print("--------")
for k,v in d1.items():
    if k in d2 and d2[k]==v:
        print(k,v)