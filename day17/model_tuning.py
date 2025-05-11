from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd

# 加载数据
df = pd.read_csv(r"E:\second_month\day12\titanic.csv")
df = df.dropna(subset=['Survived', 'Age'])
X = df[['Pclass', 'Age', 'SibSp', 'Fare']]
y = df['Survived']

# 数据划分
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 定义模型和参数网格
model = LogisticRegression()
param_grid = {'C': [0.1, 1, 10], 'max_iter': [100, 200, 300]}

# 使用 GridSearchCV 进行超参数搜索
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5)
grid_search.fit(X_train, y_train)

# 打印最优参数与评估结果
print("Best Parameters: ", grid_search.best_params_)
best_model = grid_search.best_estimator_
print("Test Accuracy: ", best_model.score(X_test, y_test))
