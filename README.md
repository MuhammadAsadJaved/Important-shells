# Important-shells

This repo contains some important python shells used for basic image/xml operations for custom datasets for deep learning models training.
The code is heavily borrowed from different internet sources. 

Seniors are welcomed for making correction / improvement.


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
