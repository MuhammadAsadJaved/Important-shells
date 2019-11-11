#Count all objects in xml files.
import cv2
import xml.etree.ElementTree as ET
import glob
import os
import numpy as np
#put all xmls in the folder and give the path as given below.

xmlPath = "xmlN/"   # Input xml file path
xmlFiles = os.listdir(xmlPath) 

no_objects=[]

for xmlFile in xmlFiles:
    tree = ET.parse(xmlPath+xmlFile)
    root = tree.getroot()

    for obj in root.findall("object"):
        no_objects.append(obj)

print(len(no_objects))


