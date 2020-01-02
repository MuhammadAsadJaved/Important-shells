# write html for visual comparison


#This is used to show all required images in xml file for the comparison of some outputs.

# 1-put input images in the images folder and all other images in some other folders
#2- Change line 47 to 51 "input, org etc" with your other images name.
#3- run the code.  it will create xml with 3 coulms and rows=no of input images. you can change accordingly. just compy and paste idex.write line
# to increate no of colums.
#Now check index.html in browser, it will show only first colums,  copy images from other folder to input images folder and refresh the page. it will show all.

# Note do not run code again when all images are in the input images folder. ti will create xml with all of them again.



import os, random



outputFolder = '/home/littro/PycharmProjects/writeImagesinXml/'
imgsPath = '/home/littro/PycharmProjects/writeImagesinXml/images/'

imgFiles = os.listdir(imgsPath)

#result_dir=imgsPath
img_w =512
img_h = 512

index_path = os.path.join(outputFolder, 'index.html')
index = open(index_path, 'w')
index.write("<html><body><table><tr>")
index.write("<th>Input</th><th>OriginalOutput</th><th>Output</th></tr>")




for sample_file in os.listdir(imgsPath):  # A -> B

    sample_file = imgsPath+sample_file




    index.write("<td><img src='%s' width='%d' height='%d'></td>" % (sample_file if os.path.isabs(sample_file) else (
            '../../..' + os.path.sep + sample_file), img_w, img_h))

    index.write("<td><img src='%s' width='%d' height='%d'></td>" % (sample_file.replace("input", "org") if os.path.isabs(sample_file.replace("input", "org")) else (
            '../../..' + os.path.sep + sample_file.replace("input", "org")), img_w, img_h))

    index.write("<td><img src='%s' width='%d' height='%d'></td>" % (sample_file.replace("input", "synthesized") if os.path.isabs(sample_file.replace("input", "synthesized")) else (
            '../../..' + os.path.sep + sample_file.replace("input", "synthesized")), img_w, img_h))

    index.write("</tr>")


index.close()



