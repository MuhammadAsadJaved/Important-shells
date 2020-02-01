"""
This shell is used to compare files in one folder with files in ohter folder. if they are not same it will delete files that 
are not same. i.e  check images and xmls and delete if images do not have corresponding xmls and vice virsa.
"""

import os 

xmlPath= "xm/"   # all xml files path 
AllImagePath= "img/" # All images path 
imgCount=0
xmlCount=0

#it will read all images in the folder and check if relevent xml is not in the xml folder it will delete that image.
for i in os.listdir(AllImagePath):
    if i.replace(".jpg", ".xml") not in os.listdir(xmlPath):

        os.remove(os.path.join(AllImagePath,i.replace(".xml", ".jpg")))
        imgCount+=1
print("Images deleted", imgCount)

#it will read all xmls in the folder and check if relevent image is not in the image folder it will delete that xml.
for i in os.listdir(xmlPath):
    if i.replace(".xml", ".jpg") not in os.listdir(AllImagePath):

        os.remove(os.path.join(xmlPath,i.replace(".jpg", ".xml")))
        xmlCount+=1
print("XMLs deleted", xmlCount)
