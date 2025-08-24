x=1
while x<=3:
    pin=int(input("enter pin="))
    if pin==1234:
        print("valid")
        break
    else:
        print("invalid,try again..")
        x+=1
        continue
if x==4:
    print("All attemps completed(3)")
print("thank you")



        
