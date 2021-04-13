#!/usr/bin/env python

"""
Predicting artists from paintings using tensorflow.keras.

"""
# data tools
import os, sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# sklearn tools
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

# parsing arguments
import argparse

# tf tools
import tensorflow
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (Conv2D, 
                                     MaxPooling2D, 
                                     Activation, 
                                     Flatten, 
                                     Dense)
from tensorflow.keras.utils import plot_model
from tensorflow.keras.optimizers import SGD
from tensorflow.keras import backend as K
from pathlib import Path

# image processing 
import cv2

# utility functions 
from viz_utils import load_data
from viz_utils import one_hot
from viz_utils import train_network
from viz_utils import model_structure_viz
from viz_utils import plot_train_hist
from viz_utils import evaluate_model


def main():
    print("\n[INFO] Initialising analysis...")
    
    # Initialise argumentparser
    ap = argparse.ArgumentParser()
    
    # Define arguments
    ap.add_argument("-it", "--infile1", required=False, help="Input path, training data", type = str, default="training")
    ap.add_argument("-iv", "--infile2", required=False, help="Input path, training data", type = str, default="validation")   
    ap.add_argument("-w", "--width", required=False, help="Width on resized images", type=int, default=32)   
    ap.add_argument("-he", "--height", required=False, help="Height on resized images", type=int, default = 32)
    ap.add_argument("-e", "--epochs", required=False, help="Train/test split", type=int, default=15)
    ap.add_argument("-b", "--batchsize", required=False, help="Batchsize in model training", type=int, default = 32)


    # Parse arguments to args
    args = vars(ap.parse_args())
    
    # fetch args
    width = args["width"]
    height = args["height"]
    epochs = args["epochs"]
    batch_size = args["batchsize"]
    
    # define input paths to train and validation data 
    path1 = os.path.join("data", args["infile1"])
    path2 = os.path.join("data", args["infile2"])
    
    

    print("\n[INFO] Fetching data...") 
    # load train and validation set
    trainX, train_Y = load_data(path1, width = width, height = height)
    testX, test_Y = load_data(path2, width = width, height = height)
    
    # get list of unique labels for classification report
    label_names = set(train_Y)
    
    print("\n[INFO] Preprocessing data...") 
    # make labels onehot encoding
    trainY = one_hot(train_Y)
    testY = one_hot(test_Y)
    
    # convert input data to tensors
    trainX = tensorflow.convert_to_tensor(trainX, dtype=tensorflow.float64)
    testX = tensorflow.convert_to_tensor(testX, dtype=tensorflow.float64)
    
    print("\n[INFO] Training model...") 
    # train network and get training history
    model_trained = train_network(trainX, trainY, testX, testY, batch_size, epochs, width = width, height = height)
    
    # make visualization of the model architecture
    model_structure_viz(model_trained)
    
    # create visualization of training
    plot_train_hist(model_trained, epochs)
    
    print("\n[INFO] Evaluating model...") 
    # create classification report
    clf_report = evaluate_model(model_trained, testX, testY, batch_size, label_names)
    print("\n Classification report:")
    print(clf_report)
    
    print("\n [INFO] ALL DONE! ") 
    
# define behaviour from command line 
if __name__=="__main__":
    main()
    
 
    
    
    
    
    
    