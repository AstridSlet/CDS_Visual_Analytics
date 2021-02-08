import os
import sys
import cv2
from pathlib import Path # for filepaths 
import numpy as np
from PIL import Image
import glob # for fetching images 
import pandas as pd # for storing image info 
import matplotlib # for saving image

# define path to image files
images_path = os.path.join(os.path.join("data"))

# create empty list to store information
height_list = []
width_list = []
nchannels_list = []
filename_list = []

# create loop that loads all files into a list - and save the file name of each file in another list
for filename in Path(images_path).glob("*.jpg"):
    im = Image.open(filename) # open file
    image = np.asarray(im) # make file into array
    height = image.shape[0] # get the height (no. of rows)
    width = image.shape[1] # get the width (no. of collumns)
    no_channels = image.shape[2] # get no. of color channels 
    file_name = Path(each_file).stem # save filename
    # append data to lists 
    height_list.append(height)
    width_list.append(width)
    nchannels_list.append(no_channels)
    filename_list.append(file_name) 

# Save info in pandas dataframe
df = pd.DataFrame(zip(filename_list, height_list, width_list, nchannels_list), 
               columns =["filename", "height", "width", "no_color_channels"]) 

# define output path name + output file name  
outpath = os.path.join("output", "image_info.csv")

# save the dataframe in the output folder (using the output path)
df.to_csv(outpath, index=False)

# create list to store the four arrays (one for each quarter of the image)
array_list = []
# create list to store which quadrant of image
name_list = ["top_left_im", "top_right_im","bottom_left_im", "bottom_right_im"]

# define image split function
def image_function(im):
    image = np.asarray(im) # make file into array
    height = image.shape[0] # get the height (no. of rows)
    width = image.shape[1] # get the width (no. of collumns)
    top_left_im = image[0:int(height/2), 0:int(width/2)]
    array_list.append(top_left_im)
    top_right_im = image[0:int(height/2), int(width/2):]
    array_list.append(top_right_im)
    bottom_left_im = image[int(height/2):, 0:int(width/2)]
    array_list.append(bottom_left_im)
    bottom_right_im = image[int(height/2):, int(width/2):]
    array_list.append(bottom_right_im)
    return array_list

# loop through images
for filename in Path(images_path).glob("*.jpg"):
    file_name = Path(filename).stem
    print(file_name)
    im_file = Image.open(filename)
    image_function(im_file)
    for i, k in zip(array_list, name_list):
        i =np.ascontiguousarray(i)
        # define output path and image name 
        outpath = os.path.join("output", f"{file_name}_{k}.jpg")
        # save image 
        matplotlib.image.imsave(f"{outpath}", i)


# Not sure if I need to include the lines below... 
if __name__ =="__main__":
    main()

