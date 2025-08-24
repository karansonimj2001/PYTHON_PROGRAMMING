import p179

def add(a,b,c):
    return a+b+c

print(add(2,3,4))
print(p179.add(10,20))

from p179 import add
print(add(10,20))

#how to import a module
    #import modulename
    #import modulename as alias

#how to import a fun from module
    #from modulename import fun1,fun2,..
    #from modulename import *
