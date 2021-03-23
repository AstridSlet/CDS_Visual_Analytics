#!/usr/bin/env python

# import packages 
import sys,os
import numpy as np
import argparse
sys.path.append(os.path.join(".."))
import pandas as pd

# import utility function
import utils.classifier_utils as clf_util

# Import sklearn metrics
from sklearn import metrics
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


def main():
    print("\nInitialising analysis...")
    
    # Initialise argumentparser
    ap = argparse.ArgumentParser()
    
    # Define arguments
    ap.add_argument("-i", "--infile", required=False, help="Input filename", type = str, default="mnist_784")
    ap.add_argument("-s", "--split", required=False, help="Train/test split", type=float, default=0.2)
    ap.add_argument("-o", "--outfile", required=False, help="Output csv filename", default = "metrics_logreg.csv")


    # Parse arguments to args
    args = vars(ap.parse_args())
    
    # fetch args
    input_name = args["infile"]
    split_value = args["split"]
    
    print("\nFetching data...")
    
    # fetch data 
    X, y = fetch_openml(input_name, return_X_y = True)
    
    # make into numpy array 
    X = np.array(X)
    y = np.array(y)
    
    # create train/test split NB you need this 0.2 to be parsed as an arg!
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = split_value)
    
    # min-max scaling the input features
    X_train_scaled = (X_train - X_train.min())/(X_train.max() - X_train.min())
    X_test_scaled = (X_test - X_test.min())/(X_test.max() - X_test.min())
    
    print("\nTraining model...")

    # train logostic regression model 
    clf = LogisticRegression(penalty='none', 
                         tol=0.1, 
                         solver='saga',
                         multi_class='multinomial').fit(X_train_scaled, y_train)
    
    
    # calculate predictions for the test set 
    y_pred = clf.predict(X_test_scaled)
    
    
    print("\nCalculated performance metrics: ")
    # calculate metrics and print in terminal 
    cm = metrics.classification_report(y_test, y_pred)
    print(cm)
    
    # create df for storing metrics
    df = pd.DataFrame(metrics.classification_report(y_test, y_pred, output_dict=True)).transpose().round(decimals=2)

    
    # Output csv filename
    outfile_name = args["outfile"]
        
    # save classification report    
    df.to_csv(os.path.join("..", "out", outfile_name), index= True)

    
# define behaviour from command line 
if __name__=="__main__":
    main()
    
 
    
    
    
    
    
    