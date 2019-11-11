
"""
Draw bounding box on single image according to it's corresponding xml's information to check 
weather label information is right or wrong.
"""
import cv2
import xml.etree.ElementTree as ET
import glob
import os
import numpy as np
xmlFile = "001.xml"  # input xml name
imgFile =cv2.imread('001.jpg')  # input image name 
xmin =[]
xmax =[]
ymin =[]
ymax = []
classes =[]
tree = ET.parse(xmlFile)
root = tree.getroot()
for obj in root.findall("object"):
    bndbox = obj.find("bndbox")
    classes.append(obj.find("name").text)
    xmin.append(int(bndbox.find("xmin").text))
    xmax.append(int(bndbox.find("xmax").text))
    ymin.append(int(bndbox.find("ymin").text))
    ymax.append(int(bndbox.find("ymax").text))
count = 0

#y= int(len(xmax))
n = 0
#for n in xmin:
while n<= len(xmax)-1:
    cv2.rectangle(imgFile, (xmin[n], ymin[n]), (xmax[n], ymax[n]), (255, 255, 0), 2)
   # print(n)
    n+=1
#for n in range(xmin.len()):
<xmin>310</xmin><xmax>381</xmax><ymin>160</ymin><ymax>237</ymax>

cv2.imwrite("rsults.jpg", imgFile)


#xmin =310
#xmax =153
#ymin =160
#ymax =237
#cv2.rectangle(im, (xmin, ymin), (xmax, ymax), (255,255,0),2)
#cv2.imwrite("test.jpg",im)

cv2.waitKey(0)
cv2.destroyAllWindows()
