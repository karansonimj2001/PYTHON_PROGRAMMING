a=2
b=3
def add():
    global a,b,c
    a=5
    b=6
    c=a+b
    print(c)

def mul():
    print(a*b)

add()
mul()
print(c)

#Local Variable:
    #bydefault all vars defined inside fun block considered as local
    #local var can be used by it's scope/block
    #for each fun call,local var gets the memory and this memory also
    #gets destroy when call is completed.

#Global Variable:
    #if a variable is not local then it is global
    #bydefault all vars defined at top level considered as gloabl
    #we can also define global var from function block using global keyword
    



