from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 初始化 WebDriver
driver = webdriver.Chrome()

try:
    # 打开登录页面
    driver.get("http://quotes.toscrape.com/login")
    time.sleep(2)  # 等待页面加载

    # 找到用户名和密码输入框
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")

    # 填写用户名和密码（随意填写，因为这是一个测试网站）
    username_input.send_keys("testuser")
    password_input.send_keys("testpassword")

    # 找到登录按钮并点击
    login_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
    login_button.click()
    time.sleep(2)  # 等待登录后页面加载

    # 循环翻页，直到没有下一页
    while True:
        try:
            # 尝试找到“下一页”按钮
            next_button = driver.find_element(By.CSS_SELECTOR, ".next a")
            next_button.click()
            time.sleep(2)  # 等待新页面加载
        except Exception as e:
            print("到最后一页了:", e)
            break

finally:
    # 关闭浏览器
    time.sleep(2)
    driver.quit()