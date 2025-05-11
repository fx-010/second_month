import schedule, time
import pandas as pd
import smtplib
from email.mime.text import MIMEText
import os

def send_report():
    # 读取汇总表
    df = pd.read_csv(r"E:\second_month\day12\miss.csv")
    avg = df['total_amount'].mean()

    # 构建邮件正文
    body = f"截至 {pd.Timestamp.today().date()}，日均订单金额：{avg:.2f}"
    msg = MIMEText(body)
    msg['Subject'] = '每日订单统计报告'
    msg['From'] = '2321933720@qq.com'
    msg['To'] = '2768169914@qq.com'

    # 发送邮件
    with smtplib.SMTP_SSL('smtp.qq.com', 465) as server:
        email = os.getenv('EMAIL_ADDRESS', '2321933720@qq.com')
        password = os.getenv('EMAIL_PASSWORD')
        if not password:
            raise ValueError("请设置环境变量 EMAIL_PASSWORD 为 QQ 邮箱授权码")
        server.login(email, password)
        server.send_message(msg)
    print("报告已发送")

schedule.every().day.at("08:00").do(send_report)

if __name__ == "__main__":
    print("定时任务已启动，等待每天 08:00 发送报告...")
    # send_report()
    while True:
        try:
            schedule.run_pending()
            time.sleep(30)
        except Exception as e:
            print(f"调度错误: {str(e)}")
            time.sleep(30)  # 出错后继续循环

# 运行
'''
win + R --> cmd
set EMAIL_PASSWORD=授权码
python e:\second_month\day12\report_email.py
'''