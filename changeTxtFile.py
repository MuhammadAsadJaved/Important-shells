#this file is used to read and change something from all .txt files from a folder 
#and write new changed .txt files in another folder.

import os
files_dir = './f/' #input directory 

out_dir = './out/' # first output directory for changed .txt
if not os.path.exists(out_dir):
    os.mkdir(out_dir)
files_list = os.listdir(files_dir)

out_files_list = os.listdir(out_dir)

for files in files_list:
    file = files_dir+files
    outputfile = out_dir+files

    with open(file) as in_file, open(outputfile, 'w') as out_file:


        data = in_file.read()
        data = data.replace(' ', '')
        data = data.replace('(', '')
        data = data.replace(')', '')
        data = data.replace(',', ' ')
        out_file.write(data)
        #print(out_file)

out_dir2 = './out2/' # second output directory for second changes .txt files
if not os.path.exists(out_dir2):
    os.mkdir(out_dir2)


for files in out_files_list:
    file2 = out_dir+files
    #print(file2)
    outputfile = out_dir2+files
    with open(file2) as in_file, open(outputfile, 'w') as out_file:

        for line in in_file:
            line = line.strip()
            a = (line[0:-1])
            b = (line[-1])
            # c = str.join(b,a)
            c = " ".join((b, a))
            #print(c)
            out_file.write(c)
            out_file.write('\n')
           # print(out_file)
#
