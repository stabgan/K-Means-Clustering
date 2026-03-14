# Data Preprocessing Template

# Importing the libraries
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split


def main():
    # Importing the dataset
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dataset = pd.read_csv(os.path.join(script_dir, "Data.csv"))
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values

    # Splitting the dataset into the Training set and Test set
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=0
    )

    # Feature Scaling
    # from sklearn.preprocessing import StandardScaler
    # sc_X = StandardScaler()
    # X_train = sc_X.fit_transform(X_train)
    # X_test = sc_X.transform(X_test)

    return X_train, X_test, y_train, y_test


if __name__ == "__main__":
    main()
