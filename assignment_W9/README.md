## Repo description 

The files found in this folder relates to the assignment of W9. 


In order to run the script you need to clone this repo by running in bash: 

`$ git clone https://github.com/AstridSlet/CDS_Visual_Analytics/assignment_W9`

You then need to create the venv __cv101__. To do this you cd into this called __assignment_W9__ folder and run:

`$ bash create_vision_venv.sh`

You then need to activate the environment by running: 

`$ source cv101/bin/activate`

You can now run the script with: 

`$ python cnn-artists.py`

You can specify the following arguments: 
* "-it", "--infile1", required=False, help="Input path, training data", type = str, default="training"
* "-iv", "--infile2", required=False, help="Input path, training data", type = str, default="validation"  
* "-w", "--width", required=False, help="Width on resized images", type=int, default=32
* "-he", "--height", required=False, help="Height on resized images", type=int, default = 32
* "-e", "--epochs", required=False, help="Train/test split", type=int, default=15
* "-b", "--batchsize", required=False, help="Batchsize in model training", type=int, default = 32

This will produce a classification report printet in the command line with f1 score for each of the five output classes (Degas, Gaugin, Monet, VanGogh and Cezanne) and saved as a csv in the output folder. Additionally the script will produce an image of the model architecture and the training history, which is also saved in the output folder. 


## Assignment description 

###Assignment 5 - CNNs on cultural image data

__Multi-class classification of impressionist painters__

So far in class, we've been working with 'toy' datasets - handwriting, cats, dogs, and so on. However, this course is on the application of computer vision and deep learning to cultural data. This week, your assignment is to use what you've learned so far to build a classifier which can predict artists from paintings.

You can find the data for the assignment here: https://www.kaggle.com/delayedkarma/impressionist-classifier-data

Using this data, you should build a deep learning model using convolutional neural networks which classify paintings by their respective artists. Why might we want to do this? Well, consider the scenario where we have found a new, never-before-seen painting which is claimed to be the artist Renoir. An accurate predictive model could be useful here for art historians and archivists!

For this assignment, you can use the CNN code we looked at in class, such as the ShallowNet architecture or LeNet. You are also welcome to build your own model, if you dare - I recommend against doing this.

Perhaps the most challenging aspect of this assignment will be to get all of the images into format that can be fed into the CNN model. All of the images are of different shapes and sizes, so the first task will be to resize the images to have them be a uniform (smaller) shape.

You'll also need to think about how to get the images into an array for the model and how to extract 'labels' from filenames for use in the classification report
