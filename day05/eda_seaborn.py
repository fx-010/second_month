import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"E:\second_month\day05\students_score.csv")

# 箱线图
plt.figure(figsize=(6,4))
sns.boxplot(data=df.drop("Name", axis=1))
plt.title("Score Distribution (Boxplot)")
plt.show()

# 热力图（相关系数）
plt.figure(figsize=(6,4))
sns.heatmap(df.drop("Name", axis=1).corr(), annot=True, cmap="coolwarm")
plt.title("Score Correlation Heatmap")
plt.show()

# 分布图
sns.displot(df["Math"], kde=True)
plt.title("Math Score Distribution")
plt.show()

map(int,input().split())