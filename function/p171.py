def show(*a):  #Var length Positional(uses tuple to manage args)
    print(a)


show()
show(10,20)
show(10,20,30,40,50)


def show(**a):  #Var length Keyword(uses dict to manage args)
    print(a)

show()
show(i=10,j=20)
show(roll=1,name='sonu',marks=67.8)
