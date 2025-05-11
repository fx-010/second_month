import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# 确保下载VADER资源
nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()# 创建了一个情感分析器对象sia

# 从文件读取文本
with open("E:\second_month\day10\sample_text.txt", "r", encoding="utf-8") as file:
    texts = file.readlines()# 把文件内容读成一个列表

# 对每句文本进行情感分析
for text in texts:
    scores = sia.polarity_scores(text)
    print(f"文本：{text.strip()}")
    print("情感得分：", scores, "\n")
