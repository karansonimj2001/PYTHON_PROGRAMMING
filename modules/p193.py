import os #perform operations related to operating system

#path=os.getcwd():returns path of current working directory
path=os.getcwd()
print(path)

#list=os.listdir():returns a list of names representing files/folders in cwd
li_names=os.listdir()
print(li_names)

#list=os.listdir(path):returns a list of names representing files/folders in given path
li_names=os.listdir("C:/abc/")
print(li_names)

#None=os.rename(src,dest)
os.rename("c:/abc/abc.txt","c:/abc/pqr.txt")
