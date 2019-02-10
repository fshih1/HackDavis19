import pandas as pd
import numpy as np
from sklearn.neighbors import LocalOutlierFactor
import math
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from keras.models import Sequential
from keras.layers import Dense
from keras import metrics
from sklearn.preprocessing import LabelEncoder
from keras.models import model_from_json
import os


# Function for calculating the probability that the
# given sample data is malignant.
def calcProb(sample):
    filename = "breast-cancer-wisconsin.data.txt"

    # Initialize datafrmae
    dataframe = pd.read_csv(filename, header=None)
    dataframe = dataframe.drop(0, 1)
    columns = ['ClTh', 'UnCeSi', 'UnCeSh', 'MaAd', 'SiEpCeSi', 'BaNu',
               'BlCh', 'NoNu', 'Mitoses', 'Class']
    dataframe.columns = columns

    # Clean out missing values
    dataframe = dataframe[dataframe.BaNu != '?']
    dataframe = dataframe.reset_index(drop=True)
    dataframe = dataframe.astype(int)

    # Clean out outliers
    LOF = LocalOutlierFactor(n_neighbors = 200)
    Local = LOF.fit_predict(dataframe.drop(['Class'], axis=1))
    dataframe['LOF_det'] = Local

    # Drop outlier column
    dataframe = dataframe[dataframe.LOF_det != -1]
    dataframe = dataframe.drop(['LOF_det'], axis=1)
    dataframe = dataframe.reset_index(drop=True)

    # Change class values from 4,2 to 1,0
    dataframe['Class'] = dataframe['Class'].replace(4, 1)
    dataframe['Class'] = dataframe['Class'].replace(2, 0)

    # Split data 80-20
    len_data = len(dataframe.index)
    len_split = math.ceil(len_data * 0.8)
    dataTest = dataframe.head(len_data - len_split)
    dataTrain = dataframe.head(len_split)

    # Get X and Y Data
    X_train = dataTrain.drop('Class', 1)
    Y_train = dataTrain.Class
    X_test = dataTest.drop('Class', 1)
    Y_test = dataTest.Class

    model = Sequential()
    model.add(Dense(3, input_dim=9, activation='relu'))
    model.add(Dense(3, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])

    # model.summary()

    fitModel = model.fit(X_train.values, Y_train.values, batch_size=10, epochs=60,
                          validation_data=(X_test.values, Y_test.values), verbose=0)

    # # load json and create model
    # json_file = open('model.json', 'r')
    # loaded_model_json = json_file.read()
    # json_file.close()
    # loaded_model = model_from_json(loaded_model_json)
    # # load weights into new model
    # loaded_model.load_weights("model.h5")
    # # print("Loaded model from disk")
    #
    # loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
    # loaded_score = loaded_model.evaluate(X_test.values, Y_test.values)
    #
    # # print("Probability of sample being malignant:")
    # predictedProb = loaded_model.predict_proba(sample.reshape(1,-1))
    predictedProb = model.predict_proba(sample.reshape(1,-1))
    # print(predictedProb[0][0])
    return predictedProb[0][0]

# calcProb(np.array([0, 1, 2, 3, 4, 5, 6, 7, 8]))
