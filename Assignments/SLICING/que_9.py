#write a python program to remove all new line in string .
string='''ello my name is karan soni,  i
 am 22 years old .
 rightnow i am learning python programming course from ducat ,
noida sector-16 ,block-A.'''
print(string)
print()
string=string.replace('''
''',"")
print(string)
