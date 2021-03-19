## Repo description 

The files found in this folder relates to the assignment of W5 (see below). 

The script takes an input image, draws a green rectancle around the text (based on four given input numbers that define the rectancle) and produces 1) an image with the rectangle drawn onto it, 2) an image cropped on the basis of that rectangle, 3) an image where the objects of the cropped image are highlighted with green using canny edge detection. 
All three images are saved in the output folder. 

The main script at this repo is called edge_detection.py

In order to run the scrip you need to create the venv __cv101__. To do this you download this folder. Then you cd into the folder and run:

`$ bash create_vision_venv.sh`

You then need to activate the environment by running: 

`$ source cv101/bin/activate`

You can now use the scrip by running: 

`$ python edge_detection.py`


The script takes the following inputs: 

* "-i", "--infile": Input filename placed in folder 'data', type = str, default = "image.png"
* "-t", "--top": No. of pixels towards top of picture from center", type = int, default=750
* "-b", "--bottom": "No. of pixels towards bottom of picture from center", type = int, default=1180
* "-l", "--left": "No. of pixels towards left of picture from center", type = int, default=800
* "-r", "--right": "No. of pixels towards right of picture from center", type = int, default=700

All arguemnts above are not required. If nothing else is specified the code will run with the example image "image.png" from the data folder. If you wish to add your own image, you simply place it in the 'data' folde rand change the -i argument to the image name. You can then play around with the four other arguments to draw the box around the text on the input image. 









## Assignment description 

###Assignment 3 - Edge detection

__Finding text using edge detection__

The purpose of this assignment is to use computer vision to extract specific features from images. In particular, we're going to see if we can find text. We are not interested in finding whole words right now; we'll look at how to find whole words in a coming class. For now, we only want to find language-like objects, such as letters and punctuation.

Download and save the image at the link below:

https://upload.wikimedia.org/wikipedia/commons/f/f4/%22We_Hold_These_Truths%22_at_Jefferson_Memorial_IMG_4729.JPG

Using the skills you have learned up to now, do the following tasks:

Draw a green rectangular box to show a region of interest (ROI) around the main body of text in the middle of the image. Save this as image_with_ROI.jpg.
Crop the original image to create a new image containing only the ROI in the rectangle. Save this as image_cropped.jpg.
Using this cropped image, use Canny edge detection to 'find' every letter in the image
Draw a green contour around each letter in the cropped image. Save this as image_letters.jpg


__General instructions__
For this exercise, you can upload either a standalone script OR a Jupyter Notebook
Save your script as edge_detection.py OR edge_detection.ipynb
If you have external dependencies, you must include a requirements.txt
You can either upload the script here or push to GitHub and include a link - or both!
Your code should be clearly documented in a way that allows others to easily follow along
Similarly, remember to use descriptive variable names! A name like cropped is more readable than crp. The filenames of the saved images should clearly relate to the original image
