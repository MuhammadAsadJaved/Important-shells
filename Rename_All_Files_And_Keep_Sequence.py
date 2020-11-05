#This program is used to copy all the files and xml files from two folders and 
#paste with new names in new location. The name of xml and images will be new but sequence will be same. 

import os, shutil



def batchRenameFile(srcDirNamexml, srcDirNameimg, destDirNamexml, destDirNameimg):
   i = 1;

   files_xml =os.listdir(srcDirNamexml)
   files_img =os.listdir(srcDirNameimg)

   for file in files_xml:
       xmlPath = srcDirNamexml+file
       imgPath =srcDirNameimg+file.replace(".xml", ".jpg")

       shutil.copy(xmlPath, destDirNamexml + '/ANNPIC' + str(i).zfill(5) + '.xml')
       shutil.copy(imgPath, destDirNameimg + '/ANNPIC' + str(i).zfill(5) + '.jpg')
       i= i+ 1


srcDirNamexml = './annN/'  #input xmls folder
srcDirNameimg = './imgN/'   #input images folder

destDirNamexml = './ResizedAnn/'    #output xmls folder
destDirNameimg =  './ResizedImgs/'  #output images folder


batchRenameFile(srcDirNamexml,srcDirNameimg, destDirNamexml, destDirNameimg)



