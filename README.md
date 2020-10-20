# Important-shells

This repo contains some important python shells used for basic image/xml operations for custom datasets for deep learning models training.
The code is heavily borrowed from different internet sources. 

Seniors are welcomed for making correction / improvement.

## Important Note:
* It is recommended to always make a copy of your data before using any shell as a little mistake may delete your files/dataset.
* The user is resonsible for any loss/problem caused by these shells. 

## Draw bounding boxes on all images

This shell is used to draw bounding boxes on all images in a folder by reading their bounding box values from xml annotations. 
Like coco formate. 

* We suppos you have images and corresponding xml annotations in two separate folder. 
* Download this shell [draw_bounding_box_on_all_images.py](https://github.com/MuhammadAsadJaved/Important-shells/blob/master/draw_bounding_box_on_all_images.py)

* Now change [imagesPath](https://github.com/MuhammadAsadJaved/Important-shells/blob/master/draw_bounding_box_on_all_images.py#L11) and [xmlPath](https://github.com/MuhammadAsadJaved/Important-shells/blob/master/draw_bounding_box_on_all_images.py#L12) 
in the [draw_bounding_box_on_all_images.py](https://github.com/MuhammadAsadJaved/Important-shells/blob/master/draw_bounding_box_on_all_images.py) file. 

* Then run using 
```
python draw_bounding_box_on_all_images.py
```
Resulted images with boudning boxes will be saved in `bbimages` folder. 

## Count number of total objects in xml annotation files. 

This shell is used to count total number of object in all xml annotations in a folder. 
For example you have coco dataset xml annotations and you want to count total number of objects
then you can use this shell. 

* We suppos you have xml annotations in a folder. 
* Download this shell first [countObjects_In_XML.py](https://github.com/MuhammadAsadJaved/Important-shells/blob/master/countObjects_In_XML.py)

* Nonw change [xmlPath](https://github.com/MuhammadAsadJaved/Important-shells/blob/master/countObjects_In_XML.py#L9) in the in the shell. 
* Then run using 

```
python countObjects_In_XML.py
```
After the calculations , it will display total number of objects. 

specific_ObjectsCounter_in_xmls.py

## Count specific number of objects in xml annotation files. 



This shell is used to count total number of object as well as total number of objects for each class in all xml annotations in a folder. 
For example you have coco dataset xml annotations and you want to count how many person, car etc objects are there
then you can use this shell. 

* We suppos you have xml annotations in a folder. 
* Download this shell first [specific_ObjectsCounter_in_xmls.py](https://github.com/MuhammadAsadJaved/Important-shells/blob/master/specific_ObjectsCounter_in_xmls.py)

* Nonw change [xmlPath](https://github.com/MuhammadAsadJaved/Important-shells/blob/master/specific_ObjectsCounter_in_xmls.py#L8) in the in the shell. 
* Currently I use only 7 classes, i.e person ,car , truck , bus , motobikes, bicycle and other, you can add more if conditions to calculate name. 
* Note: The name should be same as name of the objects in the xml file, otherwise it will ignore in counting. 

* Then run using 

```
python specific_ObjectsCounter_in_xmls.py
```
After the calculations , it will display total number of objects , number of objects for each class 
and total number of objects other than these classes. 

## Delete single object from all xml annotations.

This shell is used to delete a single object from all xml annotations in a folder. 
For example if xmin is > xmax , that's mean this bounding box value have some problem 
So you want to detelee this kind of all objects, or some similar conditions. 
Then you can use this shell. 
* We suppos you have xml annotations in a folder. 
* Download [Delete_single_object.py](https://github.com/MuhammadAsadJaved/Important-shells/blob/master/Delete_single_object.py)
* Change [input](https://github.com/MuhammadAsadJaved/Important-shells/blob/master/Delete_single_object.py#L9) and [output](https://github.com/MuhammadAsadJaved/Important-shells/blob/master/Delete_single_object.py#L10) xmls path. 
* You can change conditions according to your need. 
* Then run using 
```
python Delete_single_object.py
```
The resulting edited xmls will be saved in the given folder
## Delete specific name objects from all xml annotations.

This shell is used to delete a specific objects by name from all xml annotations in a folder.
For example you want to delte all 'person' objects or all 'car' objects from all xmls in a folder

Then you can use this shell. 
* We suppos you have xml annotations in a folder. 
* Download [delete_objects_in_xml_by_name.py](https://github.com/MuhammadAsadJaved/Important-shells/blob/master/delete_objects_in_xml_by_name.py)
* Change [input](https://github.com/MuhammadAsadJaved/Important-shells/blob/master/delete_objects_in_xml_by_name.py#L8) and [output](https://github.com/MuhammadAsadJaved/Important-shells/blob/master/delete_objects_in_xml_by_name.py#L9) folder path. 
* then change object names you want to delte , Note: The name should be same according to the xml. 
* Then run using 
```
python delete_objects_in_xml_by_name.py
```
The resulting edited xmls will be saved in the given folder


## Count and delete xml annotations that do not have objects. 

Sometimes the xml annotations do not have any objects and it create problems during taining AI model. 
So by running this shell you can see/delete xmls that do not have any objects. 

* We suppos you have xml annotations in a folder. 
* Download [count&Delete_XML_Dont_Have_objects.py](https://github.com/MuhammadAsadJaved/Important-shells/blob/master/count%26Delete_XML_Dont_Have_objects.py)
* Change [input path](https://github.com/MuhammadAsadJaved/Important-shells/blob/master/count%26Delete_XML_Dont_Have_objects.py#L9)
* if you only want to print xmls names then run program without uncommenting line [30](https://github.com/MuhammadAsadJaved/Important-shells/blob/master/count%26Delete_XML_Dont_Have_objects.py#L30) if you want also delete the file then uncomment line [30](https://github.com/MuhammadAsadJaved/Important-shells/blob/master/count%26Delete_XML_Dont_Have_objects.py#L30)
* Note: it is recommended to first only print file names, then verify a few and then delete by uncomming line 30. 

* Then run using 
```
python count&Delete_XML_Dont_Have_objects.py
```
The resulting edited xmls will be saved in the given folder

https://github.com/MuhammadAsadJaved/Important-shells/blob/master/rename_objects_in_xml.py

## Rename objects in xml annotations.

This shell is used to rename specific objects in xml annotations. 
For example you want to rename `padestrian` to  `person` in xml annotations. 
Then you can use this shell. 


* We suppos you have xml annotations in a folder. 
* Download [rename_objects_in_xml.py](https://github.com/MuhammadAsadJaved/Important-shells/blob/master/rename_objects_in_xml.py)
* Change [input path](https://github.com/MuhammadAsadJaved/Important-shells/blob/master/rename_objects_in_xml.py#L8) and [output_path](https://github.com/MuhammadAsadJaved/Important-shells/blob/master/rename_objects_in_xml.py#L9)

* Chane names you want to rename from line [21](https://github.com/MuhammadAsadJaved/Important-shells/blob/master/rename_objects_in_xml.py#L21) to line [29](https://github.com/MuhammadAsadJaved/Important-shells/blob/master/rename_objects_in_xml.py#L29)

* Then run using 
```
python rename_objects_in_xml.py
```
The resulting edited xmls will be saved in the given folder

