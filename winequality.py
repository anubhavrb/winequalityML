import pandas as pd
import numpy as np

"""
Master function that calls the read_file, standardize, and shuffle_data
functions.
"""
def get_preprocessed_dataset(filename):
    df = read_file(filename)
    standardize(df)
    df = shuffle_data(df)
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
Function that shuffles the dataset.
"""
def shuffle_data(df):
    return df.reindex(np.random.permutation(df.index))

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
