import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_data():

    data = pd.read_csv("dataset/KDDTrain+.csv", header=None)

    encoder = LabelEncoder()

    # convert ALL text columns to numbers
    for column in data.columns:
        if data[column].dtype == "object":
            data[column] = encoder.fit_transform(data[column])

    return data