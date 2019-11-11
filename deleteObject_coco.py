#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#This shell is used to delete or keep some specific objects in the xmls. i.e only keep person and delete other objects.
 
import os
import xml.etree.ElementTree as ET
 
origin_ann_dir = 'person/'
new_ann_dir = 'person/'
 
a = 10
for dirpaths, dirnames, filenames in os.walk(origin_ann_dir):
  for filename in filenames:
    if os.path.isfile(r'%s%s' %(origin_ann_dir, filename)):
      origin_ann_path = os.path.join(r'%s%s' %(origin_ann_dir, filename))
      new_ann_path = os.path.join(r'%s%s' %(new_ann_dir, filename))
      tree = ET.parse(origin_ann_path)
  
      root = tree.getroot()
      for obj in root.findall('object'):
        name = str(obj.find('name').text)
 
        if (name == "person" or  name == "bicycle" or name == "car" or name == "motorbike" or name == "bus" or name == "truck"):
          #root.remove(obj) 
          a=11
        else:
          root.remove(obj) 
       # if (name == "aeroplane" or  name == "train" and name == "boat" and name != "motorbike" and name != "bus" and name != "truck"):
        #  root.remove(obj)
  
      tree.write(new_ann_path)

print("Done")
