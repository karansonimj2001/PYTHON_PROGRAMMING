#write a python program to print a dictionary in table format.

d = {'a':100,'b':200,'c':300}
print("------------------------|")
print("key","|","value","|",sep="\t")
print("------------------------|")
for k,v in d.items():
    print(k,"|",v,"|",sep="\t")
print("------------------------|")