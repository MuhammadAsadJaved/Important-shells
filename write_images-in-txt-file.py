#This program will write all images from a sepecific folder with their path in a .txt file.  For example .txt file required as a reference to train during Ruyi program for coverting .caffe model to .wk file.

import os

path = "E:\\HiSVP_PC_V1.2.2.0\\software\\data\\detection\\images\\asad\\SecurityVIS\\train\\"
with open("asad-SecurityVIS-image_ref_list.txt", "w", encoding="utf-8") as filewrite:
    for r, d, f in os.walk(path, "*.txt"):
        for file in f:
            fil = path+ file
            filewrite.write(fil+ "\n")
           
