# Given a Folder path in a Directory Structure. E.g. “temp/reg”; you need to find all the files with extensions “.c” in this folder as well as in the sub-folders.
#Assume its in C drive

#the use of os is to interact with your operating system, to create folders, remove folders, move folders
import os

for file in os.listdir('C:/tmp/reg'):
    #returns a list containing the names of the entry in the given path
    if file.endswith(".c"):
        #if file ends with that
        print(file)


