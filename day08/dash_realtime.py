import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# 1️⃣ 读取数据（此处为静态文件，实际可用定时任务更新）
df = pd.read_csv(r"E:\second_month\day08\realtime_sales.csv")

# 2️⃣ 初始化 Dash 应用
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("实时销售数据仪表板"),
    dcc.Interval(
        id='interval-component',
        interval=10*1000,  # 每10秒更新一次
        n_intervals=0
    ),
    dcc.Graph(id='live-update-graph')
])

@app.callback(
    Output('live-update-graph', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_graph_live(n):
    # 模拟数据更新（实际中可读取最新数据）
    df_updated = pd.read_csv(r"E:\second_month\day08\realtime_sales.csv")
    fig = px.line(df_updated, x="Time", y="Sales", title="实时销售趋势")
    return fig

if __name__ == '__main__':
    app.run(debug=True)
