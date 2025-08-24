#5 ways of parameter definition
    #Positional only
    #Keyword only
    #Positional or Keyword
    #Variable length Positional
    #Variable length Keyword

def show(a,b,/): #Positional only
    print(a,b)

show(2,3)
#show(a=2,b=3)   #error


def show(*,a,b):#Keyword only
    print(a,b)

show(a=2,b=3)
#show(2,3)       #error


def show(a,b):  #Positional or Keyword
    print(a,b)


show(2,3)
show(a=2,b=3)




