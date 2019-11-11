#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#This shell is used to delete or keep some specific objects in the xmls. i.e only keep person and delete other objects.
import os
import xml.etree.ElementTree as ET
 
origin_ann_dir = 'xmls/'   #input folder
new_ann_dir = 'new_xmls/'  #output folder
 
for dirpaths, dirnames, filenames in os.walk(origin_ann_dir):
  for filename in filenames:
    if os.path.isfile(r'%s%s' %(origin_ann_dir, filename)):
      origin_ann_path = os.path.join(r'%s%s' %(origin_ann_dir, filename))
      new_ann_path = os.path.join(r'%s%s' %(new_ann_dir, filename))
      tree = ET.parse(origin_ann_path)
  
      root = tree.getroot()
      for object in root.findall('object'):
        name = str(object.find('name').text)
        if (name == "tricycle" ):
          root.remove(object)
        if (name == "bicycle" ):
          root.remove(object)
        if (name == "awning-tricyle" ):
          root.remove(object)
        if (name == "motor" ):
          root.remove(object)

      tree.write(new_ann_path)
