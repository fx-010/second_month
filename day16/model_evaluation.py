import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score, f1_score

# 加载数据
df = pd.read_csv(r"E:\second_month\day12\titanic.csv")
df = df.dropna(subset=['Survived', 'Age'])  # 去除缺失值
X = df[['Pclass', 'Age', 'SibSp', 'Fare']]  # 特征
y = df['Survived']  # 目标

# 数据划分
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 建立模型
model = LogisticRegression()
model.fit(X_train, y_train)

# 预测与评估
y_pred = model.predict(X_test)

# 打印评估指标
print("AUC: ", roc_auc_score(y_test, y_pred))
print("F1-score: ", f1_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
