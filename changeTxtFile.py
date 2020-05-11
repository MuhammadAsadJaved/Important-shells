
import os
files_dir = './f/'

out_dir = './out/'

files_list = os.listdir(files_dir)
if not os.path.exists(out_dir):
    os.mkdir(out_dir)
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

for files in files_list:
    file = files_dir+files
    outputfile = out_dir+files

    with open(file) as in_file, open(outputfile, 'w') as out_file:

        for line in in_file:
            line = line.strip()
            a = (line[0:-1])
            b = (line[-1])
            # c = str.join(b,a)
            c = " ".join((b, a))
            print(c)
            out_file.write(c)
            out_file.write('\n')
            print(out_file)

