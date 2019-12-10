#count number of files in a flder 

import os 


Filespath = "CroppedFinalImgs"  #Input directory 

no =len(os.listdir(Filespath))

print(no)
