import os
print(os.getcwd()) #CWD= Current working directory//Returns the present working directory
print(os.getcwdb())#Returns the present working directory as a byte object

os.chdir('C:\\Users\\Aryan\\Documents\\PYTHON\\study\\FileTest') #use to change directory
print(os.listdir()) #All files and sub directories inside a directory
                    # can be known using the listdir() method
print(os.getcwd())

#use to make a new directory 
os.mkdir('Test')

#use to rename a directory
os.rename('Test','New_One')

#Removing a file and directory
os.remove('vvvv.c') #use to remove a file
os.rmdir('New_One') #use to remove a directory

os.chdir('C:\\Users\\Aryan\\Documents\\PYTHON\\study')



