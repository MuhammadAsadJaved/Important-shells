
import numpy as np
import scipy.misc
#import cv2
import os
import matplotlib.pyplot as plt
 
path = "numpy_files/"  #path to numpy files folder
npy_list = os.listdir(path)
save_path = "numpy_output/" #path to save coverted images
#output_name = os.path.splitext(os.path.basename("output"))[0]  
if not os.path.exists(save_path):
    os.mkdir(save_path)
 
for i in range(0, len(npy_list)):
    print(i)
    print(npy_list[i])
    npy_full_path = os.path.join(path, npy_list[i])
    img = np.load(npy_full_path) 
 
    #save_full_path = os.path.join(save_path, npy_list[i][:-4])
    #scipy.misc.imsave(save_full_path, img +".jpg")
    #disp_to_img = scipy.misc.imresize( img , [512, 512])  
    plt.imsave(os.path.join(save_path, "{}.png".format(npy_list[i].replace(".npy",""))), img, cmap='plasma')

