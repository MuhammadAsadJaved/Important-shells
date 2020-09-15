'''
Read a txt file line by line and createa separate file for each line
here we use first colum as  aname and other coloms are xmin , ymin, xmax and ymax coordinates
from the txt file. 
the txt file looks like this
output_0006.png 91 101 281 222 1.0
output_0007.png 88 119 304 212 1.0
output_0008.png 73 126 319 211 1.0
output_0009.png 43 114 301 224 1.0
output_0010.png 76 101 278 215 1.0


'''
name_list = []
bottom =[]
left = []
width  =[]
height = []


with open('./detectionALL.txt') as in_file:

    for line in in_file:
        #print(line)

        line = line.split(" ")
        firstCol = line[0]
        name_list.append(firstCol)
        bot = line[1]
        bottom.append(bot)
        lef = line[2]
        left.append(lef)
        w = line[3]
        width.append(w)
        h = line[4]
        height.append(h)
        #print(firstCol)

for i in range(0, len(name_list)):
    name = name_list[i].replace('.png', '.txt')
    print(name)
    with open(name, 'w') as out_file:
        xmin = left[i]
        ymin = bottom[i]
        xmax = width[i] #+left[i])
        xmax  = int(xmax)+int(xmin)
        ymax = height[i] #+ bottom[i]
        ymax = int(ymax)+ int(ymin)
        #print(xmax)
        #print(ymax)
        clas = '0'

        line = " ".join((clas, xmin, ymin, str(xmax) , str(ymax )))

        #print(line)

        #out_file.write('0', " " , xmin , " ", ymin , " " ,xmax, " ", ymax)
        out_file.write(line)
        #print(out_file)





#print(name_list[0])
