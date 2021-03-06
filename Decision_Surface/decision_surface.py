"""
====================================================
Plot the decision surface on the Windturbine dataset
====================================================

Can Ozgur Parlak
canparlak@gmail.com

Lehrstuhl fuer Windenergietechnik
Universitaet Rostock
"""
print(__doc__)

import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from matplotlib.colors import ListedColormap

# Parameters
n_classes = 3
plot_colors = "ryb"
plot_step = 0.02

# Create color maps
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

# Load data
data = np.loadtxt("D:/Ek Bellek/Masterarbeit/Machine Learning/NumberOfBlades/python/decision_surface/data.txt",delimiter=',')
target = np.loadtxt("D:/Ek Bellek/Masterarbeit/Machine Learning/NumberOfBlades/python/decision_surface/target.txt",dtype='int32')
target_names = np.load('D:/Ek Bellek/Masterarbeit/Machine Learning/NumberOfBlades/python/decision_surface/target_names.npy')

feature_names = []
infile = open('E:/Machine Learning/NumberOfBlades/python/decision_surface/feature_names.txt','r')
for line in infile:
    feature_names.append(line.strip())
infile.close()

for pairidx, pair in enumerate([[0, 1], [0, 3], [0, 2],
                                [1, 3], [1, 2], [2, 3]]):
    # We only take the two corresponding features
    X = data[:, pair]
    y = target

    # Train
    clf = DecisionTreeClassifier().fit(X, y)

    # Plot the decision boundary
    plt.subplot(2, 3, pairidx + 1)

    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, plot_step),
                         np.arange(y_min, y_max, plot_step))
    plt.tight_layout(h_pad=0.5, w_pad=0.5, pad=2.5)

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    cs = plt.contourf(xx, yy, Z, cmap=plt.cm.RdYlBu)

    plt.xlabel(feature_names[pair[0]])
    plt.ylabel(feature_names[pair[1]])

    # Plot the training points
    for i, color in zip(range(n_classes), plot_colors):
        idx = np.where(y == i)
        plt.scatter(X[idx, 0], X[idx, 1], c=color, label=target_names[i],
                    cmap=plt.cm.RdYlBu, edgecolor='black', s=15)

##plt.suptitle("Entscheidungsbaum")
plt.legend(loc='lower right', borderpad=0, handletextpad=0)
plt.axis("tight")
plt.show()
