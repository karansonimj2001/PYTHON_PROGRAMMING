'''Write a Python program to get the top three items in a shop.
Sample data: {'item1':45.50,'item2':35,'item3':41.30,'item4':55,'item5':24}
Expected Output:
item4 55
item1 45.5
item3 41.3'''
dict1={'item1':45.50,'item2':35,'item3':41.30,'item4':55,'item5':24}
sorting=sorted(dict1.values(),reverse=True)
print(sorting)
sorting1=sorting[:3]
print(sorting1)
dict2={}

for k in sorting1:
    for i , j in dict1.items():
        if k==j:
            dict2[i]=j
print(dict2)       
    # for j in dict1():
