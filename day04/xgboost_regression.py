import pandas as pd
import xgboost as xgb  # 建模
from sklearn.model_selection import train_test_split  # 拆分数据
from sklearn.metrics import mean_squared_error  # 评估
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_csv(r"E:\second_month\day04\house_prices.csv")
X = df[['Area']]  # 特征：房屋面积
y = df['Price']   # 目标：房价

# 正确拆分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=42)

# 构建 XGBoost 回归模型
model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=10, random_state=42)
model.fit(X_train, y_train)

# 预测与评估
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)  # 均方误差（MSE）
print("均方误差 (MSE):", mse)

# 可视化结果
plt.scatter(X_test, y_test, color='blue', label="Actual Price")
plt.plot(X_test, y_pred, color='red', label="Predicted Price")
plt.xlabel("Area (sqft)")
plt.ylabel("Price ($)")
plt.title("XGBoost Regression: House Price Prediction")
plt.legend()
plt.show()