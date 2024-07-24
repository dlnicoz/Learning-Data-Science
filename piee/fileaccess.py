# f = open("whileloops.py" , "rt")
# print(f.read())
# f.close()

# acces and write into file
# f = open("whileloops.py",'a')
# f.write("hi hello from coding")
# f.close()
#
# f = open("whileloops.py","r")
# print(f.read())

import os 
if os.path.exists("whileloops.py"):
    os.remove("whileloops.py")
else:
    print("file does not exists")
