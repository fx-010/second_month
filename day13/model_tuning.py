import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler

# 读取并预处理
df = pd.read_csv(r"E:\second_month\day12\titanic.csv")
df['Sex'] = df['Sex'].map({'male':1,'female':0})
# 只对X的数值列计算均值并填充缺失值
X = df[["Pclass","Sex","Age","SibSp","Parch","Fare"]]
numeric_cols = X.select_dtypes(include=np.number).columns
X = X.copy()
X[numeric_cols] = X[numeric_cols].fillna(X[numeric_cols].mean())
y = df["Survived"]

# 模型定义
log_reg = LogisticRegression(max_iter=200)
rf = RandomForestClassifier()

# 网格搜索参数设置
param_grid_lr = {# 逻辑回归的超参数网格
    'C': [0.1, 1, 10],# 正则化强度的倒数，值越小正则化越强（防止过拟合）
    'solver': ['liblinear', 'saga']# 优化算法，liblinear 适合小数据集，saga 适合大数据集
}
param_grid_rf = {# 随机森林的超参数网格
    'n_estimators': [50, 100],# 树的数量
    'max_depth': [5, 10, None]# 树深
}

# 交叉验证
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# 逻辑回归调参
grid_lr = GridSearchCV(log_reg, param_grid_lr, cv=cv, scoring='accuracy')
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
grid_lr.fit(X_scaled, y)
print("Best Logistic Regression Model: ", grid_lr.best_params_)
print("Classification Report: \n", classification_report(y, grid_lr.predict(X_scaled)))

# 随机森林调参
grid_rf = GridSearchCV(rf, param_grid_rf, cv=cv, scoring='accuracy')
grid_rf.fit(X, y)
print("Best Random Forest Model: ", grid_rf.best_params_)
print("Classification Report: \n", classification_report(y, grid_rf.predict(X)))
