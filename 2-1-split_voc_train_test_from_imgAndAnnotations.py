# -*- coding:utf-8 -*-
"""
This file is used to create train.txt and val.txt which stores imgage numbers. this only create train.txt so we need to 
manually coppy about 15 to 20 % names into val.txt file. then run Conver_xmlToTxt_voc_label.py file whic will create train.txt file
to train the darknet.

Put all images in the JPEGImages folder and xmls into the Annotation folder before running this shell.

"""
import os
from os import listdir, getcwd
from os.path import join
if __name__ == '__main__':
    #images path
    source_folder='/darknet/build/darknet/x64/data/vocN/VOCdevkit/VOC2007/JPEGImages/'
    dest='/darknet/build/darknet/x64/data/vocN/VOCdevkit/VOC2007/ImageSets/Main/train.txt' 
    dest2='/darknet/build/darknet/x64/data/vocN/VOCdevkit/VOC2007/ImageSets/Main/val.txt'  
    file_list=os.listdir(source_folder)       
    train_file=open(dest,'a')                 
    val_file=open(dest2,'a')                  
    for file_obj in file_list:                
        file_path=os.path.join(source_folder,file_obj) 
        
        file_name,file_extend=os.path.splitext(file_obj)
        
        file_num=str(file_name) 
          
        if(file_num > 1000):                                 #print file_num
            train_file.write(file_name+'\n')  
        else :
            val_file.write(file_name+'\n')    
    train_file.close()
val_file.close()

