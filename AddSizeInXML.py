#in some xmls' annotations, the size is missing mistakenly, and give an error during YOLO annoataions conversion, 
#So first check all xmls's if the size is missing , then add size according to the rquirements, 
#Note: Here we add fixed size i.e h=576, w=720 if it's  missing. You can loop over the images directory and add the exact size of each image.
#run  $python AddSizeInXML.py
import os
import xml.etree.ElementTree as ET

origin_ann_dir = 'xml/'  # xmls input path
new_ann_dir = 'new_xmls/'  # xmls output path

for dirpaths, dirnames, filenames in os.walk(origin_ann_dir):
    for filename in filenames:
        if os.path.isfile(r'%s%s' % (origin_ann_dir, filename)):
            origin_ann_path = os.path.join(r'%s%s' % (origin_ann_dir, filename))
            new_ann_path = os.path.join(r'%s%s' % (new_ann_dir, filename))
            tree = ET.parse(origin_ann_path)

            root = tree.getroot()
            for size in root.findall("size"):
                #name = str(object.find('name').text)

                width = int(size.find("width").text)
                height = int(size.find("height").text)
                if (width == 0):
                    print(filename)
                    width = "720"

                if (height == 0):
                    (print(filename0
                    height = "576"

                #print(width, height, )
                size.find("width").text = width
                size.find("height").text = height


            tree.write(new_ann_path)
