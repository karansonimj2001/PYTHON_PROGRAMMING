import os
print(os.path.exists("test.txt"))#returns True if file exists in cwd else False
print(os.path.exists("p1.py"))

t=os.path.getctime("p1.py") #returns total seconds from created time
print(t)

import time
print(time.ctime(t)) #covert given seconds to date
