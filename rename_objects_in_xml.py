#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#Rename some objects in xmls. i.e change car to var in all exmls. 
import os
import xml.etree.ElementTree as ET

origin_ann_dir = 'xmls/' #Input xmls folder
new_ann_dir = 'new_xmls/'    #Output xmls folder
 
 
for dirpaths, dirnames, filenames in os.walk(origin_ann_dir):
  for filename in filenames:
    if os.path.isfile(r'%s%s' %(origin_ann_dir, filename)):
      origin_ann_path = os.path.join(r'%s%s' %(origin_ann_dir, filename))
      new_ann_path = os.path.join(r'%s%s' %(new_ann_dir, filename))
      tree = ET.parse(origin_ann_path)
  
      root = tree.getroot()
      for object in root.findall('object'):
        name = str(object.find('name').text)
        if (name == "pedestrian" ):
          name = "person"  
        if (name == "van" ):
          name = "car"  
        if (name == "truck" ):
          name = "car"  
        if (name == "bus" ):
          name = "car"        
	object.find('name').text = name 
  
      tree.write(new_ann_path)
