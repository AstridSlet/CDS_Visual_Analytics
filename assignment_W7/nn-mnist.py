#!/usr/bin/env python

# import packages 
import sys,os
import numpy as np
sys.path.append(os.path.join("..", "..", ".."))
import argparse
import pandas as pd

import utils.classifier_utils as clf_util

# Import sklearn metrics
from sklearn import metrics
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from utils.neuralnetwork import NeuralNetwork
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split


def main():
    print("\nInitialising analysis...")
    
    # Initialise argumentparser
    ap = argparse.ArgumentParser()
    
    # Define arguments
    ap.add_argument("-i", "--infile", required=False, help="Input filename", type = str, default="mnist_784")
    ap.add_argument("-s", "--split", required=False, help="Train/test split", type=float, default=0.2)
    ap.add_argument("-o", "--outfile", required=False, help="Output csv filename", default = "metrics_nn.csv")
    ap.add_argument("-e", "--epochs", required=False, help="Number of epochs", type = int, default = 1000)



    # Parse arguments to args
    args = vars(ap.parse_args())
    
    # fetch args
    input_name = args["infile"]
    split_value = args["split"]
    n_epochs = args["epochs"]

    
    print("\nFetching data...")
    
    # fetch data 
    digits = datasets.load_digits()
    
    # convert to floats
    data = digits.data.astype("float")
    
    # perform min-max regularization
    data = (data - data.min())/(data.max() - data.min())
    
    # create train/test split NB you need this 0.2 to be parsed as an arg!
    X_train, X_test, y_train, y_test = train_test_split(data, 
                                                        digits.target, 
                                                        test_size = split_value)
    
    #scaling the input features
    X_train_scaled = (X_train - X_train.min())/(X_train.max() - X_train.min())
    X_test_scaled = (X_test - X_test.min())/(X_test.max() - X_test.min())
    
    # convert labels from integers to vectors
    y_train = LabelBinarizer().fit_transform(y_train)
    y_test = LabelBinarizer().fit_transform(y_test)
    
    
    print("\nTraining network...")

    # train logostic regression model 
    nn = NeuralNetwork([X_train.shape[1], 20, 15, 10]) # no. of input features, hiddenlayer1, hiddenlayer2, no. of output features
    nn.fit(X_train, y_train, epochs = n_epochs)
    
    # calculate predictions for the test set and print in terminal
    predictions = nn.predict(X_test_scaled)
    predictions = predictions.argmax(axis=1)
    print("\nCalculated performance metrics: ")
    print(metrics.classification_report(y_test.argmax(axis=1), predictions))
    
    # create df for storing metrics
    df = pd.DataFrame(metrics.classification_report(y_test.argmax(axis=1), 
                                                    predictions, 
                                                    output_dict=True)).transpose().round(decimals=2)

    # Output csv filename
    outfile_name = args["outfile"]
        
    # save classification report    
    df.to_csv(os.path.join("..", "out", outfile_name), index = True)

    
# define behaviour from command line 
if __name__=="__main__":
    main()
     
 
    
    
    
    
    
    