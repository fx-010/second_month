import random
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# User-Agent 列表，用于伪装不同的浏览器
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
]

# 初始化 CSV 文件
csv_file = open('quotes_safe.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['引言', '作者'])  # 写入表头

# 设置 Selenium WebDriver
options = Options()
options.add_argument(f"user-agent={random.choice(user_agents)}")  # 随机选择 User-Agent
options.add_argument("--headless")  # 无头模式（可选，不显示浏览器窗口）
driver = webdriver.Chrome(options=options)

try:
    driver.get("https://quotes.toscrape.com")
    time.sleep(random.uniform(1, 3))  # 随机等待 1-3 秒

    while True:
        # 查找当前页面的所有引言元素
        try:
            quote_elements = driver.find_elements(By.CLASS_NAME, 'quote')
            if not quote_elements:
                print("本页没有找到引言。")
                break

            # 提取引言和作者
            for quote in quote_elements:
                try:
                    quote_text = quote.find_element(By.CLASS_NAME, 'text').text
                    author = quote.find_element(By.CLASS_NAME, 'author').text
                    csv_writer.writerow([quote_text, author])
                    print(f"已保存：{quote_text[:30]}... 作者：{author}")
                except NoSuchElementException:
                    print("错误：无法找到引言或作者。")
                    continue

            # 检查是否有下一页
            try:
                next_button = driver.find_element(By.CSS_SELECTOR, 'li.next > a')
                next_button.click()
                time.sleep(random.uniform(1, 3))  # 点击后随机等待 1-3 秒
            except NoSuchElementException:
                print("没有更多页面可爬取。")
                break

        except TimeoutException:
            print("错误：页面加载超时。")
            break
        except Exception as e:
            print(f"未知错误：{str(e)}")
            break

finally:
    # 清理资源
    csv_file.close()
    driver.quit()
    print("爬取完成，数据已保存到 quotes_safe.csv")
    