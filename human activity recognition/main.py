# py main.py -p "C:\denFiles\git\introduction-to-ai\human activity recognition" -k 2
#print(classification_report(test_y, yhat, target_names=label_dict.keys()))

# import the necessary packages
import os
import numpy as np
import pandas as pd
import argparse
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report


def read_data(path, filename):
    # reading a set of preprocessed data
    return pd.read_csv(os.path.join(path, filename))


def load_dataset(label_dict, path, train_filename, test_filename):
    # load and save dataset
    train_X = read_data(path, train_filename).values[:, :-2]
    train_y = read_data(path, train_filename)['Activity']
    # substituting each value in a Series (train_y) with another value, derived from dict (label_dict)
    train_y = train_y.map(label_dict).values
    test_X = read_data(path, test_filename).values[:, :-2]
    test_y = read_data(path, test_filename)
    test_y = test_y['Activity'].map(label_dict).values
    return train_X, test_X, train_y, test_y


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", required=True, help="path to input dataset")
ap.add_argument("-k", "--neighbors", type=int, default=1, help="# of nearest neighbors for classification, "
                                                               "needed in case of using k-NN algorithm")
ap.add_argument("-j", "--jobs", type=int, default=-1, help="# of jobs for K-NN distance "
                                                           "(-1 uses all available cores),"
                                                           "needed in case of using k-NN algorithm")
ap.add_argument("-c", "--regularization_param", type=int, default=1, help="The strength of the regularization "
                                                                          "is inversely proportional to C. "
                                                                          "Must be strictly positive,"
                                                                          "needed in case of using SVC algorithm")
ap.add_argument("-ker", "--kernel_type", type=str, default="rbf", help="Specifies the kernel type to be used in "
                                                                       "the algorithm. It must be one of ‘linear’,"
                                                                       "‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’."
                                                                       "needed in case of using SVC algorithm ")
ap.add_argument("-g", "--gamma", type=str, default="scale", help="Kernel coefficient for ‘rbf’, ‘poly’ and ‘sigmoid’."
                                                                 "It must be one of ‘scale’, ‘auto’"
                                                                 "needed in case of using SVC algorithm ")
args = vars(ap.parse_args())

# grab the dataset
label_dict = {'WALKING': 0, 'WALKING_UPSTAIRS': 1, 'WALKING_DOWNSTAIRS': 2, 'SITTING': 3, 'STANDING': 4, 'LAYING': 5}
train_X, test_X, train_y, test_y = load_dataset(label_dict, args["path"], 'train.csv', 'test.csv')

# train k-NN classifier
model = KNeighborsClassifier(n_neighbors=args["neighbors"], n_jobs=args["jobs"])
model.fit(train_X, train_y)

# evaluate k-NN classifier
yhat = model.predict(test_X)
print(classification_report(test_y, yhat, target_names=label_dict.keys()))

# train SVC classifier
model = SVC(C=args["regularization_param"], kernel=args["kernel_type"], gamma=args["gamma"])
model.fit(train_X, train_y)

# evaluate k-NN classifier
yhat = model.predict(test_X)
print(classification_report(test_y, yhat, target_names=label_dict.keys()))