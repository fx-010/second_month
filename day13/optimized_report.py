import schedule
import time
import pandas as pd
import smtplib
from email.mime.text import MIMEText
import os 

def generate_report():
    # 读取汇总数据
    df = pd.read_csv(r"E:\second_month\day13\sales_dashboard.csv")  
    total_sales = df['Sales'].sum()
    
    # 动态生成报告内容
    report_content = f"今日报告：\n\n总订单金额：{total_sales:.2f}\n"
    report_content += "订单详情：\n" + df.to_string(index=False)
    
    # 发送邮件
    msg = MIMEText(report_content)
    msg['Subject'] = '自动化每日报告'
    msg['From'] = '2321933720@qq.com'
    msg['To'] = '2768169914@qq.com'

    with smtplib.SMTP_SSL('smtp.qq.com', 465) as server:
        email = os.getenv('EMAIL_ADDRESS', '2321933720@qq.com')
        password = os.getenv('EMAIL_PASSWORD')
        if not password:
            raise ValueError("请设置环境变量 EMAIL_PASSWORD 为 QQ 邮箱授权码")
        server.login(email, password)
        server.send_message(msg)
    print("报告已发送")

schedule.every().day.at("15:10").do(generate_report)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(30)
