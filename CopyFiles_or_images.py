
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

