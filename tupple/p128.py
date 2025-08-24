#list cloning/copying
#creating a list using existing one
#3 techniques
    #1. Reference copying
    #2. Shallow copying
    #3. Deep copying

x=[1,2,[3,4]]
y=x                #reference copying
z=x.copy()         #shallow copying

import copy
d=copy.deepcopy(x) #deep copying
x[0]=10
x[-1][-1]=40
print(x)
print(y)
print(z)
print(d)
