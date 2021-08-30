"""
file is a place where we use to store our text or binary files.
we use to open the file using the f=open("file_name","mode","buffer")
once we open a file we can read to it, write to it or append to it.
then we have to close the file. f.close()
if we use mode as 'w' - it will delete all the content present from before
'r'- read mode, it will read the file completely from begining to the end.py
'a'-append mode, current contents of the file will not be deleted and new content is added in the end
'w+' - we acn write as well as read from the file
'r+'- we can read, write or append into the file
'a+' -appending and reading the
'x' -exclusive creation mode. a new file is created

for working on binary date we use to add b into the mode like 'wb','ab' etc
"""