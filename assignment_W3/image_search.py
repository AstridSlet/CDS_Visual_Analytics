#!/usr/bin/env python

import os
import sys
from pathlib import Path # for filepaths 
import cv2 # computing and comparing histograms
import pandas as pd # for saving data 


# define function that creates histogram and normalizes values
def hist_norm_function(image):
    histogram = cv2.calcHist([image], [0,1, 2], None, [8,8,8], [0, 256, 0, 256, 0, 256])
    hist_norm = cv2.normalize(histogram, histogram, 0,255, cv2.NORM_MINMAX)
    return hist_norm

def main():
    # Define data filepath
    images_path = os.path.join("data")

    # Define output filepath
    outpath = os.path.join("output", "image_info.csv")

    # make empty lists to store filenames, histograms + chi sqared values
    filename_list = []
    hist_list = []
    chi_list = []

    # define target image 
    target_image = cv2.imread(os.path.join("target_image_0001.jpg"))

    # make target image histogram
    target_histogram = hist_norm_function(target_image)
    
    # loop over images
    for each_file in Path(images_path).glob("*.jpg"):
        # get filename
        file_name = Path(str(each_file))
        print(file_name)
        # load image
        image = cv2.imread(str(file_name))
        # save filename
        filename_list.append(file_name.stem)
        # compute histogram (8 bins)
        histogram = hist_norm_function(image)
        # save histograms 
        hist_list.append(histogram)
    # compare histograms to target_histogram (CHI^2)
    for hist in hist_list:
        CHI_value = round(cv2.compareHist(target_histogram, hist, cv2.HISTCMP_CHISQR), 2)
        print(CHI_value)
        chi_list.append(CHI_value)
    # save data
    df = pd.DataFrame(zip(filename_list, chi_list), 
               columns =["filename", "distance"])
    df.to_csv(outpath, index=False)    
    
# Define behaviour when called from command line
if __name__=="__main__":
    main()
