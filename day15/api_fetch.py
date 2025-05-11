import requests
import pandas as pd

# 获取数据
resp = requests.get("https://jsonplaceholder.typicode.com/posts")
data = resp.json()

# 转为 DataFrame
df = pd.DataFrame(data)

# 统计各用户发帖数
counts = df.groupby('userId').size().reset_index(name='post_count')
print(counts)

# 保存
counts.to_csv("user_post_counts.csv", index=False)
