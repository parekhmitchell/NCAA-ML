# Data Preprocessing Program

# Importing the libraries
import NCAAClassification as nc
import pandas as pd
import os

# Importing the dataset
path = os.getcwd().replace('src', 'data\\')
dataset = pd.read_csv(path + 'complete_data.csv')
X = dataset.iloc[0:153, 2:23].values
y = dataset.iloc[0:153, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Applying PCA
from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
X_train = pca.fit_transform(X_train)
X_test = pca.transform(X_test)
explained_variance = pca.explained_variance_ratio_

# Performing various classification techniques
cmLGR = nc.logRegress(X_train, y_train, X_test, y_test)
cmSVM = nc.svm(X_train, y_train, X_test, y_test)
cmRFC = nc.rfor(X_train, y_train, X_test, y_test)