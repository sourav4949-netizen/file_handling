#open the file for writing
f=open("my_file.txt","w")
print("Enter text: (type # when done)")
s=""
while s!='#':
    s=input("Enter text")
    f.write(s+'\n')

f.close()