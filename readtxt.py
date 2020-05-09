
import os

files_dir = './f/'
files_list = os.listdir(files_dir)
result=[]
for files in files_list:
    file = files_dir+files
    f= open(file,'rt')
    data = f.read()
    data = data.replace(' ', '')
    data = data.replace('(', '')
    data = data.replace(')', '')
    data = data.replace(',', ' ')
    f.close()
    f = open(file, "wt")
    f.write(data)
    print(file)
    print(data)
    f.close()

# #Rearrange text
#
#     for line in data.splitlines():
#         cols = line.split(' ')
#         cols = cols[4:] + cols[0:4] #[cols[0]] +[cols[1]] + [cols[2]] + [cols[3]]
#         result.append(cols)
#
# print(result)
#
#
# #Rearrange text 2
# with open('002.txt', 'r') as file:
#     #text = file.read()
#     #result = []
#     for line in file:
#         line=line.strip()
#         print(line[0:-1])
#         print(line[-1])

        #print(line.strip()[-1])