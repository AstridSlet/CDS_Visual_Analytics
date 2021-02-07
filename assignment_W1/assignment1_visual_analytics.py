import os
import sys
import cv2
from pathlib import Path # for filepaths 
import numpy as np
from utils.imutils import jimshow
from PIL import Image
import glob

# define image paths 
images_path = os.path.join(os.path.join("data"))

# check that you reach the files
for each_path in Path(images_path).glob("*.jpg"):
    print(filename)


####### load files
#for filename in Path(images_path).glob("*.jpg"):
 #   im = Image.open(filename)
  #  image = np.asarray(im)
   # print(image.shape[1]) # check that is is arrays 


# create empty list to store information
height_list = []
width_list = []
nchannels_list = []
filename_list = []

# create loop that loads all files into a list - and save the file name of each file in another list
for each_file in Path(images_path).glob("*.jpg"):
    im = Image.open(filename)
    image = np.asarray(im)
    height = image.shape[0] # get the height (no. of rows)
    width = image.shape[1] # get the width (no. of collumns)
    no_channels = image.shape[2] # get no. of channels
    file_name = Path(each_file).stem # save filename
    # append data to lists 
    height_list.append(height)
    width_list.append(width)
    nchannels_list.append(no_channels)
    filename_list.append(file_name) 


print(height_list)





filenames = ["file1.npy", "file2.npy", "file3.npy"]
combined_data = np.array([np.load(fname) for fname in filenames])


# define function 
def image_function2(image, move_x, move_y):
    # define translation matrix
    N = np.float64([[1, 0, move_x],
                   [0, 1, move_y]])
    # perform translation
    image_moved = cv2.warpAffine(image, N, (image.shape[1], image.shape[0]))
    # return translated image
    return image_moved




# what is this??? why did he put it here?!?!?!
def main():
    for image in image_directory:
        shifted = translate(image, 0, 100)
        shift.imwrite()




# the lines below needs to be the final two lines bc every time you import a function from another 
# you want to tell the program that it should not ???

# if script is being called from command line
if __name__ =="__main__":
    # then execute the function called main()
    main()




if __name__ =="__main__":
    main()


