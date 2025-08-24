import os
#os.remove("test.txt") #shift+del File,error if file not found
#os.rmdir("test")  #shift+del directory,error if not found or dir is not empty

import shutil
#shutil.rmtree("test") #shift+del dir,no matter it is empty or not
tup=shutil.disk_usage("c:/") #(total,used,free) in bytes
print(tup)
print(tup[0]/1024/1024/1024)

#shutil.copy('c:/abc/pqr.txt','pqr.txt')#src,dest copy+paste
shutil.move('c:/abc/pqr.txt','pqr.txt')#src,dest  cut+paste
