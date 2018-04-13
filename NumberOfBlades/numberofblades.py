"""
=======================================================================
Plot the decision surface of a decision tree on the Windturbine dataset
=======================================================================

Can Ozgur Parlak
canparlak@gmail.com

Lehrstuhl für Windenergietechnik
Universitaet Rostock

"""
print(__doc__)

import numpy as np
from sklearn import tree
from sklearn.metrics import accuracy_score
import graphviz 

data = np.loadtxt("D:/Ek Bellek/Masterarbeit/Machine Learning/NumberOfBlades/python/dummy/data.txt",delimiter=',')
target = np.loadtxt("D:/Ek Bellek/Masterarbeit/Machine Learning/NumberOfBlades/python/dummy/target.txt",dtype='int32')
target_names = np.load('D:/Ek Bellek/Masterarbeit/Machine Learning/NumberOfBlades/python/dummy/target_names.npy')

feature_names = []
infile = open('D:/Ek Bellek/Masterarbeit/Machine Learning/NumberOfBlades/python/dummy/feature_names.txt','r')
for line in infile:
    feature_names.append(line.strip())
infile.close()

print(feature_names)
print(target_names)
print(data[0])
print(target[0]) # zero means 1-Blade

test_idx = [3, 32, 48]

#train data
train_target = np.delete(target, test_idx)
train_data = np.delete(data, test_idx, axis=0)

#testing data
test_target = target[test_idx]
test_data = data[test_idx]

clf = tree.DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=2,
            max_features=None, max_leaf_nodes=100,
            min_impurity_decrease=0.0, min_impurity_split=None,
            min_samples_leaf=3, min_samples_split=3,
            min_weight_fraction_leaf=0.0, presort=True, random_state=None,
            splitter='best')
clf.fit(train_data, train_target)

print(test_target)
print(clf.predict(test_data))
print(accuracy_score(test_target, clf.predict(test_data)))

# viz code

dot_data = tree.export_graphviz(clf, out_file=None, 
                    feature_names=feature_names,  
                    class_names=target_names,  
                    filled=True, rounded=True,  
                    special_characters=False)  
graph = graphviz.Source(dot_data)  
graph.render("NumberOfBlades")
graph
