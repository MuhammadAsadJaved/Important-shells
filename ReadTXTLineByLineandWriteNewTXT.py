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

#xmin = botom
#ymin = left
#xmax = xmin +width 
#ymax = ymax +heigh 
#407 30 277 210  0029.jpg

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
        xmin = float(bottom[i])
        ymin = float(left[i])
        xmax = float(width[i]) #+left[i])
        #xmax  = int(xmax)+int(xmin)
        xmax  = xmax+xmin
        ymax = float(height[i]) #+ bottom[i]
        #ymax = int(ymax)+ int(ymin)
        ymax = ymax+ ymin
        #print(xmax)
        #print(ymax)
        clas = '0'

        line = " ".join((clas, str(xmin), str(ymin), str(xmax) , str(ymax)))

        #print(line)

        #out_file.write('0', " " , xmin , " ", ymin , " " ,xmax, " ", ymax)
        out_file.write(line)
        out_file.write('\n')
        #print(out_file)





#print(name_list[0])
