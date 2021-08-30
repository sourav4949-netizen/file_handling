import os,sys
if os.path.isfile('my_file.txt'):
    f=open("my_file.txt","r")
    
else:
    print("The file doesnot exists")
    sys.exit()
s=f.read()
print(s)
f.close()