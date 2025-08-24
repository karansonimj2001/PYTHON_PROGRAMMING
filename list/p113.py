x=[10,20,30]
print(x)

#how to add a value to the last of list
x.append(50)
print(x)

#how to add multiple values
#x.append(1,2,5)  #error
x.append([1,2,5]) #it will be appended as nested list
print(x)

x.extend([1,2,5]) #it will append individual values to list
print(x)

#how to add a value on specific position
x.insert(1,100) #pos,value 
print(x)

#Note:performence wise insert is not a good option because it shifts
#further elements that causes slow execution of operation











