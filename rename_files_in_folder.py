"""

Rename all files in a folder , the file names will start from value 
specified in count i.e count=0 , the lenght of file name is defined in zfill().
i.e according to this the first file will be 000001 and so on. 

"""

import os
path = "/home/fqlovetb/data"   #Files/images directory . Note it will rename the files in the same folder. so create a backup
                               #if you want to keep original file names as well

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
