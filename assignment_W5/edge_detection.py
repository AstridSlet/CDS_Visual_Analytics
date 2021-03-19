# ! /usr/bin/python

# import packages
import os
import sys
import cv2
import numpy as np
import argparse 


# define image saving function
def im_save(im, image_name):
    outpath = os.path.join("output", f"{image_name}.png")
    cv2.imwrite(outpath, im)

    
    
# define main function
def main():
    
    # initialise argumentparser
    ap = argparse.ArgumentParser()
    
    # define input arguments
    ap.add_argument("-i", "--infile", required=False, help="Input filename placed in folder 'data'", type = str, default="image.png")
    ap.add_argument("-t", "--top", required=False, help="No. of pixels towards top of picture from center", type = int, default=750)
    ap.add_argument("-b", "--bottom", required=False, help="No. of pixels towards bottom of picture from center", type = int, default=1180)
    ap.add_argument("-l", "--left", required=False, help="No. of pixels towards left of picture from center", type = int, default=800)
    ap.add_argument("-r", "--right", required=False, help="No. of pixels towards right of picture from center", type = int, default=700)

    # parse arguments to args
    args = vars(ap.parse_args())
    
    # make output folder if it does not exist 
    if not os.path.exists("output"):
        os.mkdir("output")
    
    # get image name 
    im_name = args["infile"]
    
    # read image
    image = cv2.imread(os.path.join("data", im_name))
    
    # define image corners 
    top = (image.shape[0]//2) - args["top"]
    bottom = (image.shape[0]//2) + args["bottom"]
    left = (image.shape[1]//2) - args["left"]
    right = (image.shape[1]//2) + args["right"]
    
    # draw rectangle and save image
    im_rectangle = cv2.rectangle(image, (right, top), (left, bottom), (0, 255, 0), 1)
    im_save(im_rectangle, "image_with_ROI")

    
    # use rectangle to crop image and save 
    cropped = image[top:bottom, left:right]
    im_save(cropped, "image_cropped")
    
    # convert image to greyscale to enable edge detection
    grey_image = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
    
    # blur image as part of edge detection
    blurred = cv2.GaussianBlur(grey_image, (5,5), 0)
    # apply canny edge detection
    canny = cv2.Canny(blurred, 120, 120)
    
    # pick out just the outer contours of the detected objects 
    (contours, _) = cv2.findContours(canny.copy(), 
                 cv2.RETR_EXTERNAL, 
                 cv2.CHAIN_APPROX_SIMPLE)
    # draw contours/edges on the image 
    im_contours = cv2.drawContours(cropped.copy(), 
                        contours,      
                         -1,           
                         (0,255,0),    
                         2)  
    
    # save image with the detected edges 
    im_save(im_contours, "image_letters")
    
    
# define behaviour when called from command line
if __name__=="__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
