import pandas as pd
import altair as alt

df = pd.read_csv(r"E:\second_month\day12\sales_interactive.csv")

base = alt.Chart(df).encode(
    x=alt.X('Month:N', sort=list(df['Month']))
)

sales_line = base.mark_line(color='blue').encode(y='Sales:Q')
profit_line = base.mark_line(color='red').encode(y='Profit:Q')

chart = alt.layer(sales_line, profit_line).resolve_scale(
    y = 'independent'
).properties(
    width=1400, height=800, title='Sales vs Profit'
).interactive()

chart.save('altair_chart.html')

