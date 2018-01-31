import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures

"""
Master function that calls the read_file, standardize, and shuffle_data
functions.
"""
def get_preprocessed_dataset(filename):
    df = read_file(filename)
    standardize(df)
    #df = df[['fixed acidity', 'volatile acidity', 'citric acid', 'chlorides','total sulfur dioxide','density','sulphates','alcohol','quality']]
    #df = df[['fixed acidity', 'volatile acidity', 'chlorides','total sulfur dioxide','density','sulphates', 'pH', 'residual sugar', 'alcohol','quality']]
    #df = select_features(df)
    df = drop_outliers(df)
    return split(df)

"""
Function to read the input csv file and return the corresponding dataframe.
"""
def read_file(filename):
    df = pd.read_csv(filename, sep = ';')
    return df

"""
Function to standardize the dataframe using z-scores.
"""
def standardize(df):
    for column in df:
        if column == 'quality':
            continue
        mu, sigma = df[column].mean(), df[column].std()
        df[column] = (df[column] - mu)/sigma

"""
Function that splits the dataset into a 60:20:20 split.
"""
def split(df):
    train, validate, test = np.split(df.sample(frac=1), [int(.6*len(df)), int(.8*len(df))])
    return (train, validate, test)

"""
Function that splits the input dataframe into its features and targets.
"""
def get_XY(df):
    return (df.loc[:, 'fixed acidity':'alcohol'], df['quality'])

"""
Function that drops outliers >= 3 or <= 3 std. deviations from the mean.
Input assumes a standardized dataset.
"""
def drop_outliers(df):
    for column in df:
        if column == 'quality':
            continue
        df = df[df[column] <= 3]
        df = df[df[column] >= -3]
    return df

"""
Function to add polynomial features to dataset.
"""
def make_poly(df, d):
    columns = df.columns
    poly = PolynomialFeatures(degree = d)
    transformed = poly.fit_transform(df)
    labels = [columns[x] for x in transformed.get_support(indices=True) if x]
    return pd.DataFrame(transformed.fit_transform(df), columns=labels)

"""
Function to select features of dataset.
"""
def select_features(df):
    df = df[['fixed acidity', 'free sulfur dioxide', 'pH', 'alcohol', 'quality']]
    return df

if __name__ == "__main__":
    get_preprocessed_dataset('winequality-red.csv')
