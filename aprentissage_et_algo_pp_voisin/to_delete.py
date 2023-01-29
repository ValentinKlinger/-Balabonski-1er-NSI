

# https://www.sharpsightlabs.com/blog/numpy-meshgrid/
# IMPORT PACKAGES
import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
# LOAD DATA
X, y =  make_moons(n_samples = 200
                   ,noise = .1
                   ,random_state = 3
                   )
# X.shape
# y.shape
# # PLOT DATA
# plt.style.use('fivethirtyeight')
# sns.scatterplot(x = X[:,0], y = X[:,1], hue = y)
# plt.show()

#-------------------------
# CREATE TRAIN & TEST DATA
#-------------------------
(X_train, X_test, y_train, y_test) = \
    train_test_split(X,
                    y,
                    test_size = .2
    )
# CREATE MESHGRID ON WHICH WE WILL RUN OUR MODEL
grid_unit_size = .02
margin = 0.25
x_min = X[:, 0].min() - margin
x_max = X[:, 0].max() + margin
y_min = X[:, 1].min() - margin
y_max = X[:, 1].max() + margin
x_range = np.arange(start = x_min, stop = x_max, step = grid_unit_size )
y_range = np.arange(start = y_min, stop = y_max, step = grid_unit_size )
x_gridvalues, y_gridvalues = np.meshgrid(x_range, y_range)
# INITIALIZE CLASSIFIER AND FIT MODEL
knn_classifier = KNeighborsClassifier(15, weights='uniform')
knn_classifier.fit(X, y)
# COMPUTE PROBABILITIES ON GRID
gridvalues_combined_tidy = \
    np.vstack([x_gridvalues.flatten(), y_gridvalues.flatten()]).T
knn_class_probabilities = \
    knn_classifier.predict_proba(gridvalues_combined_tidy)
probability_postive_class = knn_class_probabilities[:,1]
# PLOT THE PROBABILITIES ON THE MESHGRID
fig = go.Figure(data=[
    go.Contour(
        x = x_range
        ,y = y_range
        ,z = probability_postive_class.reshape(x_gridvalues.shape)
        ,colorscale = 'RdBu'
        #,alpha = .3
    )
])
fig.show()
