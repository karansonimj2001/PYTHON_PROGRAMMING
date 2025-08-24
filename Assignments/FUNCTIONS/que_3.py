#write  the functon to find out whether entered number is prime or not.
  
def prime_notprime(num): 
    if num <= 1: 
        return False
    for i in range(2,num): 
        if num % i == 0: 
            return "it is  not a prime number "   
    return "it is a prime number "
  
num=int(input("enter the number here : "))
print(prime_notprime(num))