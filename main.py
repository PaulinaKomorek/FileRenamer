
import os

path = input("Please enter folder path ")
old = input("Please enter the fragment of file name to replace ")
new = input("Please enter the fragment of file name to replace with ")

for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)):
        os.rename(os.path.join(path, file), os.path.join(path, file.replace(old, new)))