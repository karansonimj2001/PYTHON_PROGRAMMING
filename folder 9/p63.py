#tax calculation
income=int(input("enter income="))
if income<=700000:
    print("tax=",0)
elif income>=700001 and income<=900000:
    print("tax=",income*.05)
elif income>=900001 and income<=1200000:
    print("tax=",income*.1)
else:
    print("tax=",income*.15)

