## Repo description 

The files found in this folder relates to the assignment of W7 (see below). 

The project contains two scripts placed in the __src__ folder:
* a script that loads an image data set an trains a logistic regression classifier to distinguish digits
* a script that loads an image data set an trains a neural network with two hidden layers to distinguish digits


In order to run the scripts you need to clone this repo by running: 

`$ git clone https://github.com/AstridSlet/CDS_Visual_Analytics`

You then need to create the venv __cv101__. To do this you cd into this called __assignment_W7__ folder and run:

`$ bash create_vision_venv.sh`

You then need to activate the environment by running: 

`$ source cv101/bin/activate`

You can now use the scripts by cd into the src folder running either of the scripts: 

* logistic regression: 
`$ python lr-mnist.py`

* neurla network: 
`$ python nn-mnist.py`

You can change the number 

All arguemnts above are not required. If nothing else is specified the code will run with the default settings. 

For the logistic regression: 
The script will run using the sklearn data set mnist_784, the train/test split will be 0.2 and the output name will be metrics_logreg.csv. 
You can change the input data set name from sklearn using the argument -i, the train/test split using -s and the output file name using -o. 

For the neural network: 
The script will run using the sklearn dataset 'digits',  the train/test split will be 0.2, the output name will be metrics_nn.csv and the number of epochs will be 1000. 

You can change the input data set name from sklearn using the argument -i, the train/test split using -s, the output file name using -o and the number of epochs using -e. 



## Assignment description 

###Assignment 4 - Classification benchmarks

__Classifier benchmarks using Logistic Regression and a Neural Network__

This assignment builds on the work we did in class and from session 6.

You'll use your new knowledge and skills to create two command-line tools which can be used to perform a simple classification task on the MNIST data and print the output to the terminal. These scripts can then be used to provide easy-to-understand benchmark scores for evaluating these models.


You should create two Python scripts. One takes the full MNIST data set, trains a Logistic Regression Classifier, and prints the evaluation metrics to the terminal. The other should take the full digits dataset, train a neural network classifier, and print the evaluation metrics to the terminal.


__Tips__
* I suggest using scikit-learn for the Logistic Regression Classifier
* In class, we only looked at a small sample of MNIST data. I suggest using fetch_openml() to get the full dataset, like we did in session 6
* You can use the NeuralNetwork() class that I introduced you to during the code along session
* I recommend saving your .py scripts in a folder called src﻿; and have your NeuralNetwork class in a folder called utils, like we have on worker02
* You may need to do some data manipulation to get the MNIST data into a usable format for your models
* If you have trouble doing this on your own machine, use worker02!

__General instructions__
For this exercise, you can upload either a standalone script OR a Jupyter Notebook
Save your script as edge_detection.py OR edge_detection.ipynb
If you have external dependencies, you must include a requirements.txt
You can either upload the script here or push to GitHub and include a link - or both!
Your code should be clearly documented in a way that allows others to easily follow along
Similarly, remember to use descriptive variable names! A name like cropped is more readable than crp. The filenames of the saved images should clearly relate to the original image
