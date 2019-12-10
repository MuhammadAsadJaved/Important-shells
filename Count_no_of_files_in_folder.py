#count number of files in a flder 

import os 


Filespath = "CroppedFinalImgs"

no =len(os.listdir(Filespath))

print(no)
