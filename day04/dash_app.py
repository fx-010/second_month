import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# 读取数据
df = pd.read_csv(r"E:\second_month\day04\sales_dashboard.csv")

# 初始化 Dash 应用
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Sales Dashboard"),
    dcc.Dropdown(
        id="metric-dropdown",
        options=[
            {"label": "Sales", "value": "Sales"},
            {"label": "Profit", "value": "Profit"}
        ],
        value="Sales"
    ),
    dcc.Graph(id="line-chart")
])

# 回调函数更新图表
@app.callback(
    Output("line-chart", "figure"),
    [Input("metric-dropdown", "value")]
)
def update_chart(selected_metric):
    fig = px.line(df, x="Month", y=selected_metric, title=f"Monthly {selected_metric} Trend", markers=True)
    return fig

if __name__ == "__main__":
    app.run(debug=True)
