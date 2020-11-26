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
no =1
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
           cv2.rectangle(img, (xmin[n], ymin[n]), (xmax[n], ymax[n]), (255, 255, 0), 2) #Draw boundig boxes 
           cv2.putText(img, classes[n], (int(xmin[n]), int(ymin[n])), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), lineType=cv2.LINE_AA)  #Draw corresponding labels on the bounding boxes from xml.
           n += 1

        count+=1
        cv2.imwrite(bbimages + "/" + xmlFile.replace(".xml", "").replace(".jpg", "")+ ".jpg",
        img)  # saving
        print('File %dth of / total %d'  % (no, len(xmlFiles)))
        print(imgPath+ "----> Done")
        b+=1
        
    no+=1
cv2.waitKey(0)
cv2.destroyAllWindows()
