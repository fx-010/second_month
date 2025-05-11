# 使用 Streamlit 构建一个简单的交互式应用，展示情感分析结果并实现动态数据展示
# 终端"streamlit run E:\second_month\day10\streamlit_sentiment.py"以运行

import streamlit as st
import pandas as pd
import plotly.express as px
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()
with open("E:\second_month\day10\sample_text.txt","r",encoding="UTF-8") as file:
    texts = file.readlines()

data = []
for text in texts:
    text = text.strip()# 以分行符分割
    scores = sia.polarity_scores(text)
    data.append({
        "text":text,
        "scores":scores['compound']# 只取scores中的'compound'这个综合得分数据
    })
df = pd.DataFrame(data)

st.title("情感分析仪表板")
st.write("展示文本情感评分，数值越高表示情感越正面。")
st.dataframe(df)

fig = px.scatter(df, x='text', y='scores', title="文本情感散点图", hover_data=['text'])
st.plotly_chart(fig)