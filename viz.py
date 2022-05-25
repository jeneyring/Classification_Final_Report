#visualization functions for Telco churn project

import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np


def visualize(X_train, y_train, X_validate, y_validate):
    metrics = []

    # loop through different values of k
    for k in range(1, 21):
                
        # define the thing
        knn = KNeighborsClassifier(n_neighbors=k)
        
        # fit the thing (remmeber only fit on training data)
        knn.fit(X_train, y_train)
        
        # use the thing (calculate accuracy)
        train_accuracy = knn.score(X_train, y_train)
        validate_accuracy = knn.score(X_validate, y_validate)
        
        output = {
            "k": k,
            "train_accuracy": train_accuracy,
            "validate_accuracy": validate_accuracy,
            "difference": (train_accuracy - validate_accuracy)
        }
        
        metrics.append(output)

    # make a dataframe
    results = pd.DataFrame(metrics)


    # plot the data
    results.set_index('k').plot(figsize = (16,9))
    plt.ylabel('Accuracy')

    plt.vlines(x= 10, ymin=0, ymax=1, linestyles='dashed')
    plt.xticks(np.arange(0,21,1))
    plt.grid()