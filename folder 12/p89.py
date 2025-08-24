#for(each) loop
for i in "python":
    print("hi",i)

print("-----------")
for i in range(5,15,2):#5,7,9,11,13
    print("hello",i)
    
print("---------")
for i in range(1,10,1):
    print(i)

print("---------")
for i in range(10,0,-2):
    print(i)

print("---------")
for i in range(2,5):
    print(i)

print("---------")
for i in range(5):
    print(i)

print("---------")
for i in range(1,5,-1):#empty seq
    print(i)

print("---------")
for i in range(5,1,1):#empty seq
    print(i)

print("---------")
for i in range(5,5,1):#empty seq
    print(i)

print("---------")
for i in range(1,5,0):#error
    print(i)

#range()
    #>returns a sequence of integer values
    #range(start,stop,step)
        #start--->inclusive
        #stop---->exclusive
        #step---->+ve(forward seq),-ve(reverse seq)
        #step can not be zero
        #start=stop,step is not zero-->empty seq

    #range(start,stop)
        #default step=1

    #range(stop)
        #default start=0
        #default step=1
    















