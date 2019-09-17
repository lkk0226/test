# -*- coding:utf-8 -*-
# @Time  : 2019/9/12 15:41
# @Author: likangkang
# @File  : sendEmail.py
import smtplib
import time
import os
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart


def sendemail():
    # 发送邮箱服务器
    smtpserver = "smtp.qq.com"
    # 发送邮箱用户名密码
    user = "727408845@qq.com"
    password = "ijpfpssloyhfbbje"
    # 发送和接收邮箱
    sender = "727408845@qq.com"
    receive = ['727408845@qq.com']
    # 发送邮件主题和内容
    subject = "Web Selenium 自动化测试报告" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # content = "<html><h1 style='color:red'>自动化测试，自学成才</h1></html>"
    # HTML邮件正文
    # msg = MIMEText(content, 'html', 'utf-8')##邮件主要内容
    msg = MIMEMultipart()
    msg['Subject'] = Header(subject, 'utf-8')    # 主题
    msg['From'] = "727408845@qq.com"
    msg['To'] = "727408845@qq.com"
    # 邮件正文内容
    msg.attach(MIMEText('这是附件发送测试……', 'plain', 'utf-8'))
    parPath = os.path.dirname(os.getcwd())  # 去掉文件名返回目录
    report_path = os.path.join(parPath, "report")  # 添加到路径
    file = os.listdir(report_path)  # 列出目录的下所有文件和文件夹
    file.sort(key=lambda fn: os.path.getmtime(report_path + "\\" + fn))  # 按时间排序
    file_name = file[-1]
    print("file_name", file_name)
    file_new = os.path.join(report_path, file[-1])  # 获取最新的文件保存到file_new
    print("file_new", file_new)
    att = MIMEText(open(file_new, 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    # 非中文附件
    # att["Content-Disposition"] = 'attachment; filename="eee.html"'
    # 中文附件
    att.add_header("Content-Disposition", "attachment", filename=("utf-8", "", file_name))
    msg.attach(att)
    # smtpObj = smtplib.SMTP()
    # smtpObj.connect('smtp.126.com"', 25)
    smtpObj = smtplib.SMTP_SSL(smtpserver, 465)    # ssl加密，默认加密端口是465
    # 登录邮箱服务器用户名密码
    smtpObj.login(user, password)

    print("Send email start...")
    smtpObj.sendmail(sender, receive, msg.as_string())
    smtpObj.quit()
    print("email send end!")

if __name__ == '__main__':
    sendemail()