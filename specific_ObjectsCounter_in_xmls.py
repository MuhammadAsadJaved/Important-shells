#!/usr/bin/env python2
# -*- coding: utf-8 -*-

 
import os
import xml.etree.ElementTree as ET

origin_ann_dir = 'input_xml/'  # Path to directory that contains xml files. 

persons =0
cars = 0
trucks =0
bicycles =0
motorbikes =0
buses = 0
others =0
for dirpaths, dirnames, filenames in os.walk(origin_ann_dir):
  for filename in filenames:
    if os.path.isfile(r'%s%s' %(origin_ann_dir, filename)):
      origin_ann_path = os.path.join(r'%s%s' %(origin_ann_dir, filename))

      tree = ET.parse(origin_ann_path)
  
      root = tree.getroot()
      for object in root.findall('object'):
        name = str(object.find('name').text)
        if (name == "person" ):
          persons+=1  
        if (name == "car" ):
          cars+=1  
        if (name == "truck" ):
          trucks+=1  
        if (name == "bus" ):
          buses+=1
        if (name == "motorbike" ):
          motorbikes+=1
        if (name == "bicycle" ):
          bicycles+=1
        if (name != "person" and  name != "bicycle" and name != "car" and name != "motorbike" and name != "bus" and name != "truck"):
          others+=1
          print name


print("Total Person Objects = ", persons)

print("Total Bicycle Objects = ", bicycles)

print("Total  Car Objects = ", cars)

print("Total Motobike Objects = ", motorbikes)

print("Total Bus Objects = ", buses)

print("Total Truck Objects = ", trucks)        

print("Total Other Objects = ", others)

total = persons+bicycles+cars+motorbikes+buses+trucks+others

print("Total Objects =  ", total)
  

