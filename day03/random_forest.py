import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# 加载数据
iris = load_iris()
X = iris.data
y = iris.target

# 数据拆分
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 创建并训练随机森林分类器
model = RandomForestClassifier(n_estimators=20,max_depth=1,random_state=10)
model.fit(X_train,y_train)

# 模型预测与评估
y_pred = model.predict(X_test)
print("分类报告：\n", classification_report(y_test, y_pred))

importances = pd.Series(model.feature_importances_,index=iris.feature_names)
sns.barplot(x=importances.values,y=importances.index)
plt.title("Feature Importances in Random Forest")
plt.show()
