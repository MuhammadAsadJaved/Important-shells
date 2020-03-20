import os
os.getcwd()
collection = "img/" #input directory , it will rename files and overwrite the existing files. so create a backup first for safe hand.
for i, filename in enumerate(os.listdir(collection)):
    os.rename(collection + filename, collection + str(i).zfill(2) + ".jpg") 
# zfill is the length of the output name for example for zfill(2) the out put will be 00.jpg , 01.jpg and so on.
