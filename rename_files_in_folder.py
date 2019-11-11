"""

Rename all files in a folder , the file names will start from value 
specified in count i.e count=0 , the lenght of file name is defined in zfill().
i.e according to this the first file will be 000001 and so on. 

"""

import os
#Files/images directory 
path = "/home/fqlovetb/data"
filelist = os.listdir(path)
count=0
for file in filelist:
    print(file)
for file in filelist:  
    Olddir=os.path.join(path,file)   
    if os.path.isdir(Olddir):   
        continue
    filename=os.path.splitext(file)[0]  
    filetype=os.path.splitext(file)[1]  
    Newdir=os.path.join(path,str(count).zfill(6)+filetype)  
    os.rename(Olddir,Newdir)
    count+=1
