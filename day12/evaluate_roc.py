import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为 SimHei
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示为方框的问题

# 读取并预处理
df = pd.read_csv(r"E:\second_month\day12\titanic.csv")
df['Sex'] = df['Sex'].map({'male':1,'female':0})
# 只对X的数值列计算均值并填充缺失值
X = df[["Pclass","Sex","Age","SibSp","Parch","Fare"]]
numeric_cols = X.select_dtypes(include=np.number).columns
X = X.copy()
X[numeric_cols] = X[numeric_cols].fillna(X[numeric_cols].mean())
'''select_dtypes 是 Pandas DataFrame 的方法，用于筛选指定数据类型的列
   include=np.number 表示只选择数值类型（包括 int64, float64 等）
   .columns:获取这个新DataFrame的列名,存储在numeric_cols中,numeric_cols是一个列名列表(如["Pclass", "Age", "SibSp", "Parch", "Fare"])
'''
y = df["Survived"]

# 交叉验证AUC
cv = StratifiedKFold(n_splits=5,shuffle=True,random_state=42)# StratifiedKFold：设置5折交叉验证，shuffle随机打乱数据，random_state=42 保证结果可复现
model = LogisticRegression(max_iter=200)# 逻辑回归模型，max_iter=200增加迭代次数确保收敛
auc_scores = cross_val_score(model,X,y,cv=cv,scoring="roc_auc")# cross_val_score：计算5折的AUC分数，scoring="roc_auc"指定评估指标为AUC
print("5折ROCAUC分数:", auc_scores,"平均：",np.mean(auc_scores))

# 绘制ROC曲线（用整个数据训练一次）
model.fit(X, y)
y_proba = model.predict_proba(X)[:,1]
fpr, tpr, _ = roc_curve(y, y_proba)
roc_auc = auc(fpr, tpr)

plt.figure(figsize=(6,4))
plt.plot(fpr, tpr, label=f"ROC curve (AUC = {roc_auc:.2f})")
plt.plot([0,1], [0,1], linestyle="--", color="gray")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("Titanic 生存预测 ROC 曲线")
plt.legend()
plt.show()