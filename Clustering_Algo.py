# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 20:33:34 2024

@author: rahma
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns

# Reload the dataset and use delimiter to separate the columns
data = pd.read_csv(r"C:\Users\rahma\Downloads\marketing_campaign.csv", delimiter='\t')




# there are few NA fields so we remove them

data = data.dropna()

# we create a spent column to see how much a user spends
data["Spent"] = data["MntWines"]+ data["MntFruits"]+ data["MntMeatProducts"]+ data["MntFishProducts"]+ data["MntSweetProducts"]+ data["MntGoldProds"]


# remove any outluiers so income below 60000 we keep
data = data[(data["Income"]<600000)]
X = data[['Income', 'Spent']]



# we scale and normalize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print(X_scaled)

# Find optimal number of clusters using elbow method and silhouette score
inertias = []
silhouette_scores = []
K = range(2, 11)

for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertias.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(X_scaled, kmeans.labels_))

# Plot elbow curve
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(K, inertias, 'bx-')
plt.xlabel('k')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal k')


# from elbow curve we find optimum cluster to be 4
optimal_clusters = 4
kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
kmeans.fit(X_scaled)


# Predict the clusters
data['Cluster'] = kmeans.predict(X_scaled)

# View the cluster assignment for the first few data points
print(data[['Income', 'Spent', 'Cluster']].head())

# Visualize the clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Income', y='Spent', hue='Cluster', data=data, palette='Set2', s=100)
plt.title('KMeans Clustering of Customers Based on Income and Spent')
plt.xlabel('Income')
plt.ylabel('Spent')
plt.show()
