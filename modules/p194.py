import os
names=os.listdir("test")
i=1
for n in names:
    os.rename(f"test/{n}",f"test/a{i}.txt")
    i+=1
print("done")
