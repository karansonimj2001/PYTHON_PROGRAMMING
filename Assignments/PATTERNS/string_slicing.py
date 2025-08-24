#string slicing
    #fetching substring with 0 to n charcters on the basis of indexs
    #syntax-->prefix[starindex:endindex:step]
    #startindex-->inclusive
    #endindex-->exclusive
    #step
        #+ve-->forward slicing
        #-ve-->reverse slicing
        #0---->error.
        #
s="python"

print(s[1:5:1])
print(s[-5:5:1])
print(s[-5:-2:1])
print(s[1:-2:1])
print(s[2:0:-1])
print(s[2:-6:-1])
print(s[-4:0:-1])
print(s[-4:-6:-1])
print(s[0:5:2])
print(s[5:0:-3])
print(s[2:2:1])#empty string.
# print(s[1:4:0])#error
# print(s[2:2:0])#error
print(s[1:5:10]) #only the start character will come .
print(s[2:5:])   #defalut step=1
print(s[2:5])    #defalut step=1
print(s[2::1])   #slice inclusive of last char in forward dir
print(s[2::-1])  #slice inclusive of last char in reverse dir
print(s[:2:1])   #default start = 0 if step is positive
print(s[:2:-1])  #defalut start =-1 if step is negative
print(s[::-1])   #reverse slicing
print(s[::1])
print(s[1:8:1])  #slice upto last character.
print(s[10:20:1])  #empty slicing.
