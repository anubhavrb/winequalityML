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
    return (df.loc[:, 'fixed acidity':'alcohol'], df['quality'])

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
