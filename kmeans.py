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

with open('dataset.csv') as v2: #arbitrary dataset
    x = []
    y =[]
    data = csv.reader(v2)
    for row in data:
        x.append(float(row[4])) #choose your x axis from data set
        y.append(float(row[6])) #choose y from dataset
    print(x)
    final = zip(x,y)
    final = list(final) #create a list of tuples for each cordinate
    print(final)
        

kmeans = KMeans(n_clusters=3) #kmeans classifer from scikitlearn
kmeans.fit(final)

centroid = kmeans.cluster_centers_ #markcentroid
label = kmeans.labels_ #mark which clasifying gorup it belongs too

print(centroid)
print(label)

colors = ["g.","r.","c.","y."] #list of colours

for i in range(len(final)):
    print("coordinate:",final[i], "label:", label[i])
    plt.plot(final[i][0], final[i][1], colors[label[i]], markersize = 10) #plot each cordinaye with colour belonging to each cluster


plt.scatter(centroid[:, 0],centroid[:, 1], marker = "x", s=150, linewidths = 5, zorder = 10) #plot each centroid

plt.show()