from fastapi import FastAPI# 用于创建 Web 服务（小型网站后台）
from pydantic import BaseModel# 来自 Pydantic,用于定义接收的数据格式
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# 定义请求模型
class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# 初始化应用与模型
app = FastAPI()
iris = load_iris()
X, y = iris.data, iris.target
model = RandomForestClassifier(n_estimators=50, random_state=42)
model.fit(X, y)

# 根路径端点
@app.get("/")
def read_root():
    return {"message": "欢迎使用鸢尾花预测 API! 请访问 /docs 查看 API 文档。"}

# 预测接口
@app.post("/predict")
def predict(features: IrisFeatures):
    data = [[
        features.sepal_length,
        features.sepal_width,
        features.petal_length,
        features.petal_width
    ]]
    pred = model.predict(data)[0]
    return {"predicted_class": int(pred), "class_name": iris.target_names[pred]}