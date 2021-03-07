import os
import sys
import cv2 
import numpy as np
from pathlib import Path # for filepaths 
import glob # for fetching images 
import pandas as pd # for storing image info 
import matplotlib as plt # for saving image
import imageio # for saving images


# create path to image files
images_path = os.path.join(os.path.join("sample"))

# create function that creates a color histogram 
def hist_function(file_name):
    image = cv2.imread(str(file_name))
    color_names = ("blue", "green", "red")
    channels = cv2.split(image)
    
    for channel, color_name in zip(channels, color_names):
        # create histogram
        hist = cv2.calcHist([channel], [0], None, [256], [0, 256])
        return hist


hist1 = hist_function(target_name)

plt.plot(hist1, "plot")



# define target image name
target_name = "image_0096.jpg"


# define function that gets target image information



# create loop that loads all files into a list - and save the file name of each file in another list
for each_file in Path(images_path).glob("*.jpg"):
    file_name = Path(str(each_file)) # get filename 
    print(file_name)
    im = cv2.imread(str(each_file)) # open file
    print(im.shape)





for channel, color_name in zip(channels, color_names):
    # create histogram
    hist = cv2.calcHist([channel], [0], None, [256], [0, 256])


# seperate image into channels
channels = cv2.split(image)
# define names of colors variable that we can use in our function
color_names = ("blue", "green", "red")


for channel, color_name in zip(channels, color_names):
    # create histogram
    hist = cv2.calcHist([channel], [0], None, [256], [0, 256])
    # plot histogram 
    plt.plot(hist, f"{color_name}")
    # set limit of x-axis (to avoid he axis looking weird)
    plt.xlim([0, 256])
# show plot
plt.show()


hist1_norm = cv2.normalize(hist1, hist1, 0,255, cv2.NORM_MINMAX)





# Save info in pandas dataframe
#df = pd.DataFrame(zip(filename_list, height_list, width_list, nchannels_list), 
 #              columns =["filename", "height", "width", "no_color_channels"]) 


data = {'First Column Name':  ['First value', 'Second value'],
        'Second Column Name': ['First value', 'Second value']}

df = pd.DataFrame (data, columns = ['First Column Name','Second Column Name',...])

print (df)


# define output path name + output file name  
outpath = os.path.join("output", "image_info.csv")

# save the dataframe in the output folder (using the output path)
df.to_csv(outpath, index=False)




# Include info for when the script is run from terminal
#if __name__ =="__main__":
 #   main()