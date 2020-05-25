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


srcDirNamexml = '/media/littro/ded08585-d8e8-4a37-9bd3-209b37b051fe/littro/LittroData/DualBand/visual/Resize/annN/1/'
srcDirNameimg = '/media/littro/ded08585-d8e8-4a37-9bd3-209b37b051fe/littro/LittroData/DualBand/visual/Resize/imgN/1/'

destDirNamexml = '/media/littro/ded08585-d8e8-4a37-9bd3-209b37b051fe/littro/LittroData/DualBand/visual/Resize/3'
destDirNameimg =  '/media/littro/ded08585-d8e8-4a37-9bd3-209b37b051fe/littro/LittroData/DualBand/visual/Resize/4'


batchRenameFile(srcDirNamexml,srcDirNameimg, destDirNamexml, destDirNameimg)



