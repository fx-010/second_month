import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为 SimHei
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示为方框的问题

df = pd.read_csv(r"E:\second_month\day01\orders.csv")

# 绘制箱线图（查看各类别订单金额分布）
plt.figure(figsize=(8, 5))
sns.boxplot(x="Category", y="Amount", data=df)
plt.title("各类别订单金额分布")
plt.show()

# 绘制热力图（订单金额相关性）
correlation_matrix = df.corr(numeric_only=True)
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("订单数据相关性热力图")
plt.show()

# 绘制分布图（订单金额分布情况）
sns.histplot(df["Amount"],
             kde=True, # 加一条平滑的密度曲线（Kernel Density Estimation），显示数据分布趋势
             bins=10)# 把金额分成 10 个区间，画成柱状图。
plt.title("订单金额分布")
plt.show()
