import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

"""
Master function that calls the read_file, standardize, and shuffle_data
functions.
"""
def get_preprocessed_dataset(filename):
    df = read_file(filename)
    target = df['quality']
    df = df.loc[:, 'fixed acidity':'alcohol']
    #df = select_features(df)
    #df = make_poly(df, 2)
    standardize(df)
    df['quality'] = target
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
    scaler = StandardScaler()
    df[list(df)] = scaler.fit_transform(df[list(df)])

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
    return (df.loc[:, df.columns != 'quality'], df['quality'])

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
    poly = PolynomialFeatures(degree = d)
    transformed = poly.fit_transform(df)
    return pd.DataFrame(transformed, columns=poly.get_feature_names(df.columns))

"""
Function to select features of dataset.
"""
def select_features(df):
    df = df[['alcohol', 'density', 'chlorides', 'volatile acidity', 'total sulfur dioxide', 'fixed acidity', 'pH', 'residual sugar']]
    return df

if __name__ == "__main__":
    get_preprocessed_dataset('winequality-red.csv')
