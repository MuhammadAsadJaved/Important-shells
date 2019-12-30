#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#This program is useful if you want to search a specific object in a xml file and delete 
# that xml file if do not have that specific object.   
import os
import xml.etree.ElementTree as ET
from xml.dom import minidom
origin_ann_dir = './Annotations/'
#new_ann_dir = './Annotations/'
count = 0




xmlFiles = os.listdir(origin_ann_dir)

for xmlFile in xmlFiles:

  file = origin_ann_dir+xmlFile
  mydoc = minidom.parse(file)

#Replace 'object' with specific string you want to use for searching

  items = mydoc.getElementsByTagName('object')
  no = len(items)
  if no==0:

   #uncommnet next line if also want to delete file
   # os.unlink(file)
    count+=1


  #print(len(items))

print("Deleted files that do not have objects =", count)
