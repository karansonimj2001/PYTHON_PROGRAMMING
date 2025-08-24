#tax calculation
#income<700000    tax=0
#income 700001 to 900000
    #0 to 300000 =0
    #300001 to 600000=5%
    #600001 to 900000=10%
#income 900001 to 120000
    #0 to 300000 =0
    #300001 to 600000=5%
    #600001 to 900000=10%
    #900001 to 120000=15%
#income above 1200000
    #0 to 300000 =0
    #300001 to 600000=5%
    #600001 to 900000=10%
    #900001 to 120000=15%
    #120000 above    =20%

income=int(input("enter income="))
if income<=700000:
    print("tax=",0)
elif income>=700001 and income<=900000:
    tax1=0     #0%
    tax2=15000 #5%
    tax3=(900000-income)*.1
    print("tax=",tax1+tax2+tax3)
elif income>=900001 and income<=1200000:
    tax1=0      #0%
    tax2=15000  #5%
    tax3=30000  #10%
    tax4=(1200000-income)*.15  #15%
    print("tax=",tax1+tax2+tax3+tax4)
else:
    tax1=0      #0%
    tax2=15000  #5%
    tax3=30000  #10%
    tax4=45000  #15%
    tax5=(income-1200000)*.2
    print("tax=",tax1+tax2+tax3+tax4+tax5)

