## Repo description 

The files found in this folder relates to the assignment of W3 (see below). To run the script download this folder and install the necessary packages found at the top of in the script:
os, sys, pathlib, cv2, pandas 

You can then run the script __image_search.py__
When the script has been run with the sample data (1300 .jpg files stored in the folder 'data') it should produce a  .csv file (which will be placed in the output folder) which contains histogram comparisons. 


## Assignment description 
__Creating a simple image search script__

Download the Oxford-17 flowers image data set, available at this link: https://www.robots.ox.ac.uk/~vgg/data/flowers/17/

Choose one image in your data that you want to be the 'target image'. Write a Python script or Notebook which does the following:

Use the cv2.compareHist() function to compare the 3D color histogram for your targer image to each of the other images in the corpus one-by-one.
In particular, use chi-square distance method, like we used in class. Round this number to 2 decimal places.
Save the results from this comparison as a single .csv file, showing the distance between your target image and each of the other images. The .csv file should show the filename for every image in your data except the target and the distance metric between that image and your target. Call your columns: filename, distance.


General instructions

For this exercise, you can upload either a standalone script OR a Jupyter Notebook
Save your script as image_search.py OR image_search.ipynb
If you have external dependencies, you must include a requirements.txt
You can either upload the script here or push to GitHub and include a link - or both!
Your code should be clearly documented in a way that allows others to easily follow along
Similarly, remember to use descriptive variable names! A name like hist is more readable than h.
The filenames of the saved images should clearly relate to the original image
