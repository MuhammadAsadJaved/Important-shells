"""
This .py file is used to crop a larege size image and it's xml into several cropped images with small size
and corresponding xmls for each newly created images accordingly.
"""
import os 
import xml.etree.ElementTree as ET
import glob 
import cv2
import numpy as np

imagesPath="img/"  #original images directory 
xmlPath = "xml/"   #original xmls directory 
ImgOutputPath= "CroppedImages/"   #Newly cropped images directory  (it will created automatically)
XmlOutputPath = "NewXml/"         #Newly cropped xmls directory   (it will created automatically)
    
xmlFiles = os.listdir(xmlPath)   
imgFiles = os.listdir(imagesPath)  
if not os.path.exists(ImgOutputPath):  
    os.mkdir(ImgOutputPath)
if not os.path.exists(XmlOutputPath): 
    os.mkdir(XmlOutputPath) 
extraPixels = 10                  #Extra pixels we want to add
for xmlfile in xmlFiles:         
    imgPath = imagesPath+xmlfile.replace(".xml",".jpg") 
    img = cv2.imread(imgPath)   
    imgR = 0
    imgC = 0

    if img.shape[0]%416==0:
        imgR = int(img.shape[0]/416)
    else:
        imgR = int(img.shape[0]/416)+1
    if img.shape[1]%416==0:
        imgC = int(img.shape[1]/416)
    else:
        imgC = int(img.shape[1]/416)+1
    print(imgR, imgC)
    xmin = []
    xmax = []
    ymin = []
    ymax = []
    classes=[]
    BigImg = np.zeros((416*imgR,416*imgC,3)) 
    BigImg[:img.shape[0],:img.shape[1], :] = img 
              
    tree = ET.parse(xmlPath+xmlfile.replace(".jpg",".xml"))   
    root = tree.getroot()            

    for obj in root.findall("object"):    
        bndbox = obj.find("bndbox")     
        classes.append(obj.find("name").text)          
        xmin.append(int(bndbox.find("xmin").text)) 
        ymin.append(int(bndbox.find("ymin").text))   
        xmax.append(int(bndbox.find("xmax").text))   
        ymax.append(int(bndbox.find("ymax").text)) 
    count=0
    zeros= np.zeros((len(xmin),1))

    for imrow in range(imgC):  
        for imcol in range(imgR):
            status  = False
            CroppedImg = BigImg[imcol*416 : imcol*416+416, imrow*416: imrow*416+416,: ]  
            height = CroppedImg.shape[0]
            width = CroppedImg.shape[1]

            
            print("Dimension ", imrow, imcol, CroppedImg.shape)
            root1 = ET.Element("annotation")  
            foldername = ET.SubElement(root1, "folder").text= XmlOutputPath.replace("/","")
            filenmae = ET.SubElement(root1, "filename").text= xmlfile.replace(".xml","").replace(".jpg","")+"_"+str(count+1)+".jpg"
            source = ET.SubElement(root1, "source")
            database =  ET.SubElement(source, "database").text="The VOC2005 Database"
            annotation =  ET.SubElement(source, "annotation").text="PASCAL VOC2005"
            flickr = ET.SubElement(source, "image").text="flickr"
            size = ET.SubElement(root1, "size")
            width = ET.SubElement(size, "width").text = str(width)
            height = ET.SubElement(size, "height").text= str(height)
            depth = ET.SubElement(size, "depth").text= "3"
            seg = ET.SubElement(root1, "segmented").text="0"
            i = 0
            ln = len(classes)

            while i<ln:
                
                
                if (xmin[i]>=(imrow)*416 and xmin[i]<=(imrow+1)*416 and xmax[i]<=(imrow+1)*416) and (ymin[i]>=(imcol)*416 and ymin[i]<=(imcol+1)*416 and ymax[i]<=(imcol+1)*416): 
                    xmn = int(xmin[i]%416)
                    xmx = int(xmax[i]%416)
                    ymn = int(ymin[i]%416)
                    ymx = int(ymax[i]%416)  
                    zeros[i]=1

                    status = True
                    obj = ET.SubElement(root1, "object")
                    name =  ET.SubElement(obj, "name").text=classes[i]
                    pose =  ET.SubElement(obj, "pose").text="Unspecified"
                    trun =  ET.SubElement(obj, "truncated").text="0"
                    difficult =  ET.SubElement(obj, "difficult").text="0"
                    bndbx =  ET.SubElement(obj, "bndbox")
                    ET.SubElement(bndbx, "xmin").text=str(xmn)
                    ET.SubElement(bndbx, "xmax").text=str(xmx)
                    ET.SubElement(bndbx, "ymin").text=str(ymn)
                    ET.SubElement(bndbx, "ymax").text=str(ymx)
                i+=1
            if status and CroppedImg.shape[0]>=416: 
                tree1 = ET.ElementTree(root1)
                count+=1
                print("Dimension ", imrow, imcol)
                tree1.write(XmlOutputPath+xmlfile.replace(".xml","").replace(".jpg","")+"_"+str(count)+".xml")   
                cv2.imwrite(ImgOutputPath+"/"+xmlfile.replace(".xml","").replace(".jpg","")+"_"+str(count)+".jpg", CroppedImg)  
                cv2.rectangle(CroppedImg, (xmn, ymn), (xmx, ymx), (255, 255, 0), 3)
    

