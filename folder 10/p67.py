#inline block
#we can write stmts of block at same line
#generally we use inline block to write single stmt
#if we write multiple stmts then we have put ; after every stmt

num=int(input("enter num="))
if num%2==0:print("even");print("mango")
else:print("odd");print("apple")

print("--------")

if num%2==0:
    print("even")
    print("mango")
else:
    print("odd")
    print("apple")
