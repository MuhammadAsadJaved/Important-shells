import csv
import os

#multiple csv files in a folder and write information of all into one txt (output.txt)

inputcsv = ('./data/annotations')
#csv_file = ('data/annotations/1.bboxes.tsv')
inputfiles  = os.listdir(inputcsv)
txtfile = ('./output.txt')

with open(txtfile, "w") as my_output_file:
    for file in inputfiles:
        filename = os.path.join(inputcsv, file)
        (dirname , fileName ) = os.path.split(file)
        (shortname, extension) = os.path.splitext(fileName)
        (shortname, extension) = os.path.splitext(shortname)
        shortname =shortname + ".jpg"
        #print(shortname)
        with open(filename, "r") as my_input_file:
            [my_output_file.write(shortname +'\t' + "".join(row) +'\n') for row in csv.reader(my_input_file)]
    my_output_file.close()

#read multiple .csv files and create corresponding multiple .txt files. 
'''
for file in inputfiles:
    filename = os.path.join(inputcsv, file)
    print(filename)
    with open(txtfile, "w") as my_output_file:
        with open(filename ,"r" ) as my_input_file:
            [my_output_file.write("".join(row) + '\n') for row in csv.reader(my_input_file)]
        my_output_file.close()
'''


#Multiple inputs from one csv file and generate one txt file containing all multiple outputs in it.

'''
csv_file = ('./validation_annotations.csv')
txt_file = ('./validation_annotations.txt')
with open(txt_file, "w") as my_output_file:
    with open(csv_file, "r") as my_input_file:
        [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
    my_output_file.close()
'''
