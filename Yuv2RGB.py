

#Convert Yuv420  image to RGB image and save output

import Image
import sys
from struct import *
import array
import os



input_folder = './img/'
output_folder = './out/'

images = os.listdir(input_folder)

for img in images:
    image_name = os.path.join(input_folder, img)

    print(image_name)




    width = 416   # Width and height should be same with yuv image
    height = 416

    y = array.array('B')
    u = array.array('B')
    v = array.array('B')
#
    f_y = open(image_name, "rb")
    f_uv = open(image_name, "rb")
    f_uv.seek(width*height, 1)
#
    image_out = Image.new("RGB", (width, height))
    pix = image_out.load()
#
    print "width=", width, "height=", height
#
    for i in range(0, height/2):
        for j in range(0, width/2):
            u.append(ord(f_uv.read(1)));
#
    for i in range(0, height/2):
        for j in range(0, width/2):
            v.append(ord(f_uv.read(1)));

    for i in range(0,height):
        for j in range(0, width):
            y.append(ord(f_y.read(1)));
#         #print "i=", i, "j=", j , (i*width), ((i*width) +j)
#         #pix[j, i] = y[(i*width) +j], y[(i*width) +j], y[(i*width) +j]
            Y_val = y[(i*width)+j]
            U_val = u[((i/2)*(width/2))+(j/2)]
            V_val = v[((i/2)*(width/2))+(j/2)]
            B = 1.164 * (Y_val-16) + 2.018 * (U_val - 128)
            G = 1.164 * (Y_val-16) - 0.813 * (V_val - 128) - 0.391 * (U_val - 128)
            R = 1.164 * (Y_val-16) + 1.596*(V_val - 128)
            pix[j, i] = int(R), int(G), int(B)

    image_out.save(output_folder + img.replace('.yuv',  '.jpg'))
# image_out.show()
