import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.pipeline import Pipeline

# 读取数据
df = pd.read_csv(r"E:\second_month\day06\sales_data.csv")

# 数据预处理：填充缺失值、编码产品类别、转换日期
df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df['Product'] = df['Product'].fillna("Unknown")
le = LabelEncoder()
df['Product_encoded'] = le.fit_transform(df['Product'])

# 构建数据处理管道（仅对 Amount 进行标准化）
pipeline = Pipeline([
    ('scaler', StandardScaler())
])

df['Amount_scaled'] = pipeline.fit_transform(df[['Amount']])# Scikit-learn需要二维数据

# 输出处理结果
print("预处理后的数据：\n", df.head())
