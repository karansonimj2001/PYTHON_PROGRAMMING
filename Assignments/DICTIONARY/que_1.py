#write a python script to sort (ascending and descending ) a dictionary by key.
counting={1:"one",5:"five",4:"four",3:"three",2:"two"}
print(counting)
counting_1=sorted(counting.items())
counting_1=dict(counting_1)
print("the ascending order :\n",counting_1)
decending=sorted(counting.items(),reverse=True)
# counting.__reversed__()
decending=dict(decending)
print("the decending order :\n",decending)

