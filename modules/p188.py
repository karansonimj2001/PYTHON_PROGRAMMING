import time
#str_currtime=time.ctime()
print(time.ctime())

#str_frmt_time=time.strftime("%directives")
print(time.strftime("%d/%m/%Y"))
print(time.strftime("%d %B,%Y %H:%M:%S"))

#None=time.sleep(sec) #suspend execution of program till given secs
time.sleep(2)

print("apple")

for i in range(1,11):
    print(18*i)
    time.sleep(.5)
