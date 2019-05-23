# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 15:26:39 2019

@author: irffy
"""


import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn.cluster import KMeans
import csv
data = input("enter name of dataset with .filename: ")
with open(data) as dataset:
    for row in dataset:
        print(row)
with open(data) as v2:
    
    x = []
    y =[]
    x_input =int(input("ener x axis: "))
    y_input = int(input("enter y axis: "))
    data = csv.reader(v2)
    for row in data:
        x.append(float(row[x_input]))
        y.append(float(row[y_input]))
    print(x)
    final = zip(x,y)
    final = list(final)
    print(final)
        
clusters = int(input("enter number of clusters: "))
kmeans = KMeans(n_clusters= clusters)
kmeans.fit(final)

centroids = kmeans.cluster_centers_
labels = kmeans.labels_

print(centroids)
print(labels)

colors = ["g.","r.","c.","y."]

for i in range(len(final)):
    print("coordinate:",final[i], "label:", labels[i])
    plt.plot(final[i][0], final[i][1], colors[labels[i]], markersize = 10)


plt.scatter(centroids[:, 0],centroids[:, 1], marker = "x", s=150, linewidths = 5, zorder = 10)

plt.show()