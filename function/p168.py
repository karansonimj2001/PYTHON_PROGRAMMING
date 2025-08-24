#3 ways of Arg Passing
    #Positional Args
    #Keyword Args
    #Default Args

def mul(a=1,b=1): #default args
    print(a*b)

mul()
mul(2)
mul(3,5)          #Positional Args
mul(a=5,b=6)      #Keyword Args
mul(b=6,a=5)
mul(5,b=6)
#mul(a=5,6)       #error:first we need to pass pos then keyword
#mul(a=5,b=6,a=8) #error:keyword arg repeated
#mul(a=5,c=7)     #error:an unexpected keyword argument 'c'

def mul(a=1,b):   #error:params without default come first then params with default
    pass
