
amount=int(input("enter amount : "))
if amount>=1000:
    amount-=50
    print(amount)
    print("50 casback added")
    promo_code=input("enter promocode = ")
    if promo_code=="bharat" or promo_code== "india":
        amount-=50
        print("50 cashback added for valid promocode")
    else:
        print("invalid promocode")
print("final amount = ",amount)