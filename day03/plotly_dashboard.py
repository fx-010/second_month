import pandas as pd
import plotly.express as px

df = pd.read_csv(r"E:\second_month\day03\sales_data.csv")

fig1 = px.line(df, x="Month", y="Sales", title="Monthly Sales Trend", markers=True)
fig1.show()

# 数据，X轴，Y轴，颜色，标题，size决定点的大小，(跟利润成正比（利润越大，点越大）)，鼠标悬停时显示（月份）
fig2 = px.scatter(df, x="Sales", y="Profit", color="Month",
                  title="Sales vs Profit", size="Profit", hover_data=["Month"])
fig2.show()
