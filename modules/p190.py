import sys #communication with interpreter
x=10
#memory_bytes=sys.getsizeof(object)
print(sys.getsizeof(x))

x="python is a funny language"
print(sys.getsizeof(x))

#list_of_paths=sys.path #path is a list type var that returns
#all paths where interpreter search for a module
print(sys.path)

sys.exit()

print("bye")
