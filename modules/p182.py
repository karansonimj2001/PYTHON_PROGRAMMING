import mypack.p179
print(mypack.p179.add(2,4))

import mypack.p179 as m
print(m.add(2,5))
print(m.mul(2,5))

from mypack import p179 as m
print(m.add(2,5))
print(m.mul(2,5))

from mypack.p179 import add
print(add(4,5))

#from module import fun
#from module import *
#from package import module
#from package.module import fun
