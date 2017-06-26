# Toolkit used for Classification

# Importing Libraries
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

# Logistic Regression Classification
def logRegress(X_train, y_train, X_test, y_test):
    # Fitting Logistic Regression to the Training set
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    
    # Predicting the Test set results
    y_pred = classifier.predict(X_test)

    # Counting accurate responses
    cm = numClose(y_test, y_pred)

    return [y_pred, cm]

# SVM Classificaiton
def svm(X_train, y_train, X_test, y_test):
    # Fitting SVM to the Training set
    classifier = SVC(kernel = 'linear', random_state = 0)
    classifier.fit(X_train, y_train)
    
    # Predicting the Test set results
    y_pred = classifier.predict(X_test)
    
    # Counting accurate responses
    cm = numClose(y_test, y_pred)

    return [y_pred, cm]

# Random Forest Classification
def rfor(X_train, y_train, X_test, y_test):
    # Fitting Random Forest Classification to the Training set
    classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
    classifier.fit(X_train, y_train)

    # Predicting the Test set results
    y_pred = classifier.predict(X_test)

    # Counting accurate responses
    cm = numClose(y_test, y_pred)
    
    return [y_pred, cm]

# Helper Method to Calculate num close
def numClose(y_test, y_pred):
    result = 0;
    for pos in range(0, len(y_test)):
        if(y_test[pos] == y_pred[pos]):
           # or
           #y_test[pos] == y_pred[pos] + 1 or
           #y_test[pos] == y_pred[pos] -1):
            result += 1
    
    return result