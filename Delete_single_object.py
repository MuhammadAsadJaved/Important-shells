#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#Delete a single object based on it's bounding box information etc in the xml.
 
import os
import xml.etree.ElementTree as ET
 
origin_ann_dir = 'xmls/' #xmls input path
new_ann_dir = 'new_xmls/'    #xmls output path
 
for dirpaths, dirnames, filenames in os.walk(origin_ann_dir):
  for filename in filenames:
    if os.path.isfile(r'%s%s' %(origin_ann_dir, filename)):
      origin_ann_path = os.path.join(r'%s%s' %(origin_ann_dir, filename))
      new_ann_path = os.path.join(r'%s%s' %(new_ann_dir, filename))
      tree = ET.parse(origin_ann_path)
  
      root = tree.getroot()
      for obj in root.findall("object"):
        bndbox = obj.find("bndbox")
        xmin = int(bndbox.find("xmin").text)
        xmax = int(bndbox.find("xmax").text)
        ymin = int(bndbox.find("ymin").text)
        ymax = int(bndbox.find("ymax").text)

        #if xmin ==0 or xmax==0 or ymin ==0 or ymax ==0:
        #  root.remove(obj)
          
        if xmin > xmax or ymin > ymax ==0:
          root.remove(obj)



      tree.write(new_ann_path)
