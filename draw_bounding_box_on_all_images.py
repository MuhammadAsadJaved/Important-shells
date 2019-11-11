"""
Draw bounding box on all images according to their corresponding xml's information to check 
weather label information is right or not.
"""

import cv2
import xml.etree.ElementTree as ET
import glob
import os
import numpy as np
imagesPath="imgs/"  # Input images path
xmlPath = "xmls/"   # Input xml file path
bbimages = "BbImages/"  # Output path

xmlFiles = os.listdir(imagesPath)  # getting xml files
imgFiles = os.listdir(xmlPath) # getting image files
if not os.path.exists(bbimages):  # if output image folder does not exist, then make output image folder
    os.mkdir(bbimages)

for xmlFile in xmlFiles:
    imgPath = imagesPath+xmlFile.replace(".xml", "jpg")
    img = cv2.imread(imgPath)

    xmin =[]
    xmax =[]
    ymin =[]
    ymax = []
    classes =[]
    tree = ET.parse(xmlPath+xmlFile.replace(".jpg", ".xml"))
    root = tree.getroot()
    for obj in root.findall("object"):
       bndbox = obj.find("bndbox")
       classes.append(obj.find("name").text)
       xmin.append(int(bndbox.find("xmin").text))
       xmax.append(int(bndbox.find("xmax").text))
       ymin.append(int(bndbox.find("ymin").text))
       ymax.append(int(bndbox.find("ymax").text))
    count = 0


    n = 0
    b =0

    while b<1:

        while n<len(xmax):
           cv2.rectangle(img, (xmin[n], ymin[n]), (xmax[n], ymax[n]), (255, 255, 0), 2)
           n += 1

        count+=1
        cv2.imwrite(bbimages + "/" + xmlFile.replace(".xml", "").replace(".jpg", "")+ ".jpg",
        img)  # saving
        b+=1

cv2.waitKey(0)
cv2.destroyAllWindows()
