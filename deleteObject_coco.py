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
 
#The first method is you can mention the objects you want to remove.

        #if (name == "tricycle" ):
        #  root.remove(object)
        #if (name == "bicycle" ):
        #  root.remove(object)
        #if (name == "awning-tricyle" ):
        #  root.remove(object)
        #if (name == "motor" ):
        #  root.remove(object)

 #The second method is you can metion the objects you want to keep and remove rest of them.
        
        if (name != "person" and  name != "bicycle" and name != "car" and name != "motor" and name != "bus"):
          root.remove(object)
          count+=1
  
      tree.write(new_ann_path)

print("Done")
