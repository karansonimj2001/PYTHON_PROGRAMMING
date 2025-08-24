#a,b---->Positional only
#e,f---->Keyword only
#c,d---->Positional or Keyword

def show(a,b,/,c,d,*,e,f):
    print(a,b,c,d,e,f)

show(1,2,3,4,e=5,f=6)
#show(1,2,c=3,4,e=5,f=6)   #error

help(len)
