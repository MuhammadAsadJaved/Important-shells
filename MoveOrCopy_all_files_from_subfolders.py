#This shell is used to copy/move all files/images from all subfolders to a new folder
#for example if there are multiple folders in ./1/ folder like /11/ , /12/ , /1n/  and each folder have multiple image files
#Then we will apply this given code.
# -*- coding: utf-8 -*

import glob 
import shutil
count = 0
    
destination_path = "./selected/"
pattern = "./1/*/*"  #to copy files with any extension 
#pattern = "./1/*/*.jpg"  #to copy only .jpg files   , you can chang extension according to your files. 
 
for img in glob.glob(pattern):
    shutil.move(img, destination_path)    #If you want to move files
    #shutil.copy(img, destination_path)    #If you want to copy files
    
    count+=1

print("Moved %s files to  %s " %(count, destination_path))
