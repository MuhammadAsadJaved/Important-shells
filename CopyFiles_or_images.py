#Read some files froma folder and coppy relevent files or images from another folder. 
#For example we want to copy images corresponding to 1.xml 2.xml 3.xml ..n.xml from a images folder which contains
#thousands of images. so we do not need to search corresponding images manually. 
import cv2
import xml.etree.ElementTree as ET
import glob
import os
import numpy as np
import shutil
FromCoppy="./coco_edited/person_img/"  # Input folder name from where need to copy files.
ToBecoppy = "./coco_edited/wrongxml/"   # Input files folder that need to be coppied.
Coppied = "./coco_edited/coppied/"  # Destination folder where need to store coppied files.

xmlFiles = os.listdir(ToBecoppy)  # getting files need to be coppied.

if not os.path.exists(Coppied):  # if output image folder does not exist, then create it.
    os.mkdir(Coppied)

for xmlFile in xmlFiles:
    imgPath = FromCoppy+xmlFile.replace(".xml", ".jpg")


    coppyPath = Coppied+xmlFile.replace(".xml", ".jpg")

    shutil.copyfile(imgPath, coppyPath)


no = len(os.listdir(Coppied))
print("Coppied  %d  files successfully"  % no)


'''
#other shutil notes
#Copy files:
shutil.copyfile("oldfile","newfile") #oldfile and newfile can only be files
shutil.copy("oldfile","newfile") #oldfile can only be a folder, newfile can be a file or a target directory
 
#Copy folder:
shutil.copytree("olddir","newdir") #olddir and newdir can only be directories, and newdir must not exist
 
#Rename file (directory)
os.rename("oldname","newname") #Files or directories use this command
 
#Mobile file (directory)
shutil.move("oldpos","newpos")
shutil.move("D:/Knowledge Daily/latest/A coupon, change your address book information, would you like to?.pdf", "D:/Knowledge Daily/past/")

'''
