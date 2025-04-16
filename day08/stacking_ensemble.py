import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import StackingClassifier
from sklearn.metrics import classification_report, accuracy_score

# 1️⃣ 加载数据集
iris = load_iris()
X = iris.data
y = iris.target

# 2️⃣ 拆分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3️⃣ 定义基模型
estimators = [
    ('rf', RandomForestClassifier(n_estimators=100, random_state=42)),
    ('gb', GradientBoostingClassifier(n_estimators=100, random_state=42))
]

# 4️⃣ 定义堆叠融合模型，以逻辑回归作为元模型
stack_clf = StackingClassifier(estimators=estimators, final_estimator=LogisticRegression())

# 5️⃣ 训练模型
stack_clf.fit(X_train, y_train)

# 6️⃣ 预测与评估
y_pred = stack_clf.predict(X_test)
print("融合模型准确率：", accuracy_score(y_test, y_pred))
print("分类报告：\n", classification_report(y_test, y_pred))
