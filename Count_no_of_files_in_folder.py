#count number of files in a flder 

import os 


Filespath = "CroppedFinalImgs"  #Input directory 

no =len(os.listdir(Filespath))

print(no)


'''
Or use this shell command

#Count number of files/images in folder and it's subfolders 

$find sequences -type f | wc -l                  #sequences is folder name.


'''
