import dash
from dash import dcc,html
import plotly.express as px
import pandas as pd

df = pd.read_csv(r"E:\second_month\day13\sales_dashboard.csv")

app = dash.Dash(__name__)

fig = px.line(df, x='Month', y=['Sales', 'Profit'], title='Sales vs Profit over Time')

# Dash 布局
app.layout = html.Div([
    html.H1("Sales and profit analysis dashboard"),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)
