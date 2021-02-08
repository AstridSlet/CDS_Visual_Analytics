## Repository description 

The files found at this repo relates to the assignment of W1 (see below). To run the script download this folder and install the necessary packages found at the top of in the script:
os, sys, cv2, pathlib, numpy, PIL, glob, pandas and matplotlib 

You can then run the script __assignment1_visual_analytics.py__
When the script has been run with the sample data (10 .jpg files stored in the folder 'data') it should produce 40 image files, that will be placed in the folder 'output'. 

Along with the images the script should produce a csv file (also found in the output folder) which contains information about the height, width and number of color channelse for each of the pictures from the data folder. 


## Assignment description 
__Basic scripting with Python__

Create or find small dataset of images, using an online data source such as Kaggle. At the very least, your dataset should contain no fewer than 10 images.

Write a Python script which does the following:
- For each image, find the width, height, and number of channels
- For each image, split image into four equal-sized quadrants (i.e. top-left, top-right, bottom-left, bottom-right)
- Save each of the split images in JPG format
- Create and save a file containing the filename, width, height for all of the new images.
