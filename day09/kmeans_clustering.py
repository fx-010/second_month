'''
K-Means:

K-Means 是一种无监督学习算法，用于将数据分成 K 个簇(cluster)
无监督：数据没有标签,算法根据数据本身的特征(相似性)自动分组
目标：让同一个簇内的数据点尽可能相似,不同簇的数据点尽可能不同


工作原理:
随机选择 K 个点作为初始簇中心(centroids)
将每个数据点分配到距离最近的簇中心,形成 K 个簇
计算每个簇的新中心(簇内数据点的均值)
重复步骤 2 和 3,直到簇中心不再变化(或达到最大迭代次数)
最终，每个数据点属于一个簇
'''
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

iris = load_iris()
X = iris.data
feature_names = iris.feature_names

kmeas = KMeans(n_clusters=3,random_state=42)
clusters = kmeas.fit_predict(X)# 集群

df = pd.DataFrame(X,columns=feature_names)
df['Cluster'] = clusters

plt.figure(figsize=(8,6))
sns.scatterplot(x=df[feature_names[0]], y=df[feature_names[1]], hue=df['Cluster'], palette='Set1')
plt.title("Iris Data - KMeans Clustering")
plt.xlabel(feature_names[0])
plt.ylabel(feature_names[1])
plt.show()