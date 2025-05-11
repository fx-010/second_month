import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# 读取并设置索引
df = pd.read_csv(r"E:\second_month\day15\sales_timeseries.csv", parse_dates=["Date"], index_col="Date")

# 重采样：按周平均
weekly = df.resample('W').mean()

# 3天滚动平均
df['Rolling3'] = df['Sales'].rolling(window=3).mean()

# 季节分解
result = seasonal_decompose(df['Sales'], model='additive', period=3)

# 可视化
plt.figure(figsize=(10,8))
plt.subplot(411); plt.plot(df['Sales'], label='原始'); plt.legend()
plt.subplot(412); plt.plot(weekly, label='周平均'); plt.legend()
plt.subplot(413); plt.plot(df['Rolling3'], label='3日滚动'); plt.legend()
plt.subplot(414); 
result.plot(); plt.tight_layout()
plt.show()
