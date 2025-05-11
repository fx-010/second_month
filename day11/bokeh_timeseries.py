import pandas as pd
from bokeh.plotting import figure, show, output_file
# ColumnDataSource 是 Bokeh 的数据结构，将 Pandas DataFrame 转换为 Bokeh 能直接使用的格式
from bokeh.models import ColumnDataSource, HoverTool

# 读取数据
df = pd.read_csv(r"E:\second_month\day11\sales_timeseries.csv", parse_dates=["Date"])
source = ColumnDataSource(df)

# 创建折线图
p = figure(x_axis_type="datetime", title="Daily Sales (Bokeh)", width=1600, height=800)
p.line("Date", "Sales", source=source, line_width=2, color="navy", legend_label="Sales")
# p.circle 在每个数据点上画一个橙色圆点，直径为 6
p.circle("Date", "Sales", source=source, size=6, color="orange")

# 添加悬停工具
# {%F} 表示完整日期格式(如 2025-04-18)
hover = HoverTool(tooltips=[("Date", "@Date{%F}"), ("Sales", "@Sales")],# 定义提示框的内容
                  formatters={"@Date": "datetime"})# 确保日期等特殊数据以正确格式显示
p.add_tools(hover)

# 输出
output_file("sales_bokeh.html")
show(p)
