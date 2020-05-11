
import os
files_dir = './in/'

# out_dir = './out/'
# if not os.path.exists(out_dir):
#     os.mkdir(out_dir)
# files_list = os.listdir(files_dir)
#
# out_files_list = os.listdir(out_dir)
#
# for files in files_list:
#     file = files_dir+files
#     outputfile = out_dir+files
#
#     with open(file) as in_file, open(outputfile, 'w') as out_file:
#
#
#         data = in_file.read()
#         data = data.replace(' ', '')
#         data = data.replace('(', '')
#         data = data.replace(')', '')
#         data = data.replace(',', ' ')
#         out_file.write(data)
#         #print(out_file)
#
# out_dir2 = './out2/'
# if not os.path.exists(out_dir2):
#     os.mkdir(out_dir2)
#
#
# for files in out_files_list:
#     file2 = out_dir+files
#     #print(file2)
#     outputfile = out_dir2+files
#     with open(file2) as in_file, open(outputfile, 'w') as out_file:
#
#         for line in in_file:
#             line = line.strip()
#             a = (line[0:-1])
#             b = (line[-1])
#             # c = str.join(b,a)
#             c = " ".join((b, a))
#             #print(c)
#             out_file.write(c)
#             out_file.write('\n')
#            # print(out_file)
# #

#get specific column from .txt file 
name_list =[]

with open('002.txt') as in_file:
    for line in in_file:
        line=line.split(" ")
        firstCol= line[0] #[0] is the first column of each line
        name_list.append(firstCol)
        #print(firstCol)


print(name_list[0])


# import csv
#
# with open('002.txt') as inf:
#
#     reader = csv.reader(inf, delimiter=" ")
#     first_col = list(zip(*reader))[0]
#     print(first_col)
