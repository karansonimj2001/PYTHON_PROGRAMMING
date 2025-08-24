#return stmt
    #it is used to return a value from function to calling stmt
    #after return function is not executed
    #it means,we can put only one return stmt in a function
    #if we do not specify return stmt then None will be default return value
def mul(a,b):
    c=a*b
    return c

res=mul(3,4)
print(res)

res=mul(10,20)
print(res)

print(mul(2,3))
