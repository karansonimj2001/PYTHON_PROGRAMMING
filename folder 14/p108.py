#string slicing
    #fetching substring with 0-N chars on the basis of index
    #syntax-->prefix[startIndex:endIndex:step]
    #startIndex--->inclusive
    #endIndex----->exclusive
    #step
        #+ve--->forward slicing
        #-ve--->reverse slicing
        #0----->error
s="python"
print(s[1:4:1])
print(s[-5:4:1])
print(s[-5:-2:1])
print(s[1:-2:1])
print(s[2:0:-1])
print(s[2:-6:-1])
print(s[-4:0:-1])
print(s[-4:-6:-1])
print(s[0:5:2])
print(s[5:0:-3])
print(s[2:2:1])   #empty substring
#print(s[1:4:0])  #error
#print(s[2:2:0])  #error
print(s[1:5:10])  #y
print(s[2:5:])    #default step=1
print(s[2:5])     #default step=1
print(s[2::1])    #slice inclusive of last char in forward dir
print(s[2::-1])   #slice inclusive of last char in reverse dir
print(s[:2:1])    #default start=0 if step is +ve
print(s[:2:-1])   #default strat=-1 if step is -ve
print(s[::-1])    #reverse slicing
print(s[1:7:1])   #slice upto last char
print(s[10:20:1]) #empty slicing













