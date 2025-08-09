#import os
#print(os.getcwd())  #get current working directory
#os.chdir("directry you need to change")

#os.mkdir("githubms3")                                            #creates new folder or directory
#os.makedirs(r"c:\Users\ELCOT\Documents\RMgit\githubms4")         #creates new folder with path
#os.rmdir("test3.txt")                                            #remove folder
#os.removedirs(r"c:\Users\ELCOT\Documents\RMgit\githubms4")       #remove foder with path
#os.rename("","")

#w=os.listdir(r"c:\Users\ELCOT\Documents\RMgit\githubms1")
#r=os.path.isfile(r"c:\Users\ELCOT\Documents\RMgit\githubms1")
#p=os.path.join("githubms1","test1.txt")
#print(r)
#print(p)
#print(w)

import os

folder="data"
if not os.path.exists(folder):
    os.mkdir(folder)
    print("Folder Created",folder)

print("Items in current dir:", os.listdir())

os.chdir(folder)
print("now in:",os.getcwd())

with open("hello.txt","w") as file:
   file.write("hello! this is muthuswamy")
   
os.rename("hello.txt","greeting.txt")
print("File size:", os.path.getsize("greeting.txt"), "bytes")