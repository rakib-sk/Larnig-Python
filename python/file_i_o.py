#import os if i delet any file
import os
f = open("/storage/emulated/0/portfolio /Python programming/i_o.text","r")
data = f.read()
print(data)
#How to read single line??
#If i went to read single line I can use var.readline()
line = f.readline()
print(line)
f.close() 
#
#
#Write file 
# "w" if i use "w" so delet all data in the file.
write_file = open("write.txt","w")
write_file.write("I am use w mode. it delet all data in file")
print(write_file) 
write_file.close()
#
#if i use "a" mode so don't delet all data in the file
file_a = open("write.txt","a")
file_a.write("\nNow i use a its not delet old data in the file")
print(file_a)
file_a.close()
#
# using "r+" its use to file read and writing. but its write fast in file
file_r = open("write.txt","r+")
file_r. write("\n now i use r+ mode. i write fast line in file")
print(file_r.read())
file_r.close()
#
#using with keyword
with open("write.txt","r") as f:
    print(f.read())

#
# os.remove(file_name) use to delet any file
os.remove("delet.txt")

