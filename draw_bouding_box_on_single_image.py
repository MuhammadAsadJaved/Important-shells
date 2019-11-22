
"""
Draw bounding box on single image according to it's corresponding xml's information to check 
weather label information is right or wrong , This script is to draw just one bounding box, for all boundix boxes use 
the other file in the repo.
"""
import cv2
import glob
import os
import numpy as np

im =cv2.imread('MVI_1532_NIR_frame25.jpg')   #Image path and name


#start and end points of bounding box,  it may used from the xml
xmin =365
xmax =420
ymin =505
ymax =543
cv2.rectangle(im, (xmin, ymin), (xmax, ymax), (255,255,0),2)

cv2.imwrite("test.jpg",im)

cv2.waitKey(0)
cv2.destroyAllWindows()
