import pandas as pd
import matplotlib.pyplot as plt

# 读取数据并转换日期格式
df = pd.read_csv(r"E:\second_month\day04\sales_timeseries.csv", parse_dates=["Date"])
df.set_index("Date", inplace=True)

# 绘制原始销售趋势图
plt.figure(figsize=(8, 4))
plt.plot(df.index, df["Sales"], marker='o', label="Sales")
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.show()

# 计算并绘制移动平均（窗口=3）
df["Moving_Avg"] = df["Sales"].rolling(window=3).mean()
plt.figure(figsize=(8, 4))
plt.plot(df.index, df["Sales"], marker='o', label="Sales")
plt.plot(df.index, df["Moving_Avg"], marker='s', linestyle='--', color='red', label="3-Day Moving Avg")
plt.title("Sales Trend with Moving Average")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.show()
