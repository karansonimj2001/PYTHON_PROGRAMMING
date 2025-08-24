#write a function to find that entered number even or odd. 
def even():
    ask=float(input("enter the number here : "))
    if ask%2==0:
        return "it is an even number " 
    else:
        return "it is a odd number"
print(even())