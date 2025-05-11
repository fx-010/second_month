import requests
import pandas as pd
import matplotlib.pyplot as plt
import time

# 配置
API_KEY = "1a2cdaa0f41953d3172e3201d771ca20"  # 替换为你的 API Key
CITIES = ["Beijing", "New York", "Tokyo", "Sydney", "Paris"]
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
'''
基础 URL:http://api.openweathermap.org/data/2.5/weather
这是 API 的核心端点，用于获取当前天气数据。
例如，访问这个端点（加上参数）会返回某个城市的天气信息。
查询参数：
URL 后面的 ?q={city}&appid={api_key}&units=metric 是查询参数，告诉服务器具体需要什么数据。参数之间用 & 分隔。

q={city}:
q 是查询城市名的参数。
{city} 是你在代码中定义的城市名（例如 Hulan,CN 或 London）
例如:q=London 表示请求伦敦的天气。
来源:API 文档中说明,q 参数支持城市名（英文或本地语言），可选加国家代码（如 London,UK）
appid={api_key}:
appid 是 API Key 参数，用于认证你的请求。
{api_key} 是你在 OpenWeatherMap 注册后获得的唯一密钥
来源:API 文档要求每次请求必须包含 appid 参数，以验证你的身份。
units=metric:
units 参数指定温度等数据的单位。
metric 表示使用摄氏度（°C）作为温度单位（以及米/秒作为风速单位）。
其他选项：
imperial：华氏度（°F）。
默认（不指定 units）：开尔文（K）。
units 是可选参数，用于控制返回数据的单位。
'''
def fetch_weather(city):
    """获取单个城市的天气数据"""
    try:
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        response.raise_for_status()  # 抛出 HTTP 错误
        data = response.json()
        return {
            "city": city,
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"]
        }
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {city}: {e}")
        return None

# 获取所有城市的天气数据
weather_data = []
for city in CITIES:
    weather_info = fetch_weather(city)
    if weather_info:
        weather_data.append(weather_info)
    time.sleep(1)  # 避免请求过快

# 转换为 DataFrame
weather_df = pd.DataFrame(weather_data)
print(weather_df)

# 保存到 CSV
weather_df.to_csv("weather_data.csv", index=False)
print("Data saved to weather_data.csv")

# 可视化
plt.figure(figsize=(10, 6))
plt.bar(weather_df["city"], weather_df["temperature"], color="skyblue")
plt.xlabel("City")
plt.ylabel("Temperature (°C)")
plt.title("Temperature in Different Cities")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()