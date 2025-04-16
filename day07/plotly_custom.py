import pandas as pd
import plotly.express as px

# 读取数据
df = pd.read_csv(r"E:\second_month\day07\sales_data.csv")

# 创建交互式折线图，添加自定义颜色与标记
fig = px.line(df, x="Month", y="Sales", title="Monthly Sales Trend", markers=True, color_discrete_sequence=["#636EFA"])
fig.update_layout(xaxis_title="Month", yaxis_title="Sales ($)")
fig.show()

# 创建交互式散点图展示销售与利润关系
fig2 = px.scatter(df, x="Sales", y="Profit", color="Month", size="Profit", hover_data=["Month"], title="Sales vs Profit")
fig2.show()
