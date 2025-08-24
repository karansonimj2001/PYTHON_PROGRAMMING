amt=int(input("enter amt="))
if amt>=1000:
    amt-=50
    print("50 cashback added")
    pc=input("enter promocode=")
    if pc=="bharat" or pc=="india":
        amt-=50
        print("50 cashback added for valid promocode")
    else:
        print("invalid promocode")
print("Final Amt=",amt)

#update the above code to accept both india & bharat as promocode
