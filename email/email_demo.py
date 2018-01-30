# encoding=utf-8
"""
SMTP:
SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。

smtplib和email两个模块:
Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


# TODO
if __name__ == '__main__':
    # 第三方 SMTP 服务
    mail_host = "yh-nlb.synacast.local"  # 设置服务器
    # mail_user = "xianduilun@163.com"  # 用户名
    mail_user = raw_input('from:')
    # mail_pass = "mail2017"  # 口令
    mail_pass = raw_input('password:')

    sender = mail_user
    # receivers = ['kevintian@pptv.com']
    receivers = []
    receivers.append(raw_input('to:'))

    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = Header("163", 'utf-8')
    message['To'] = Header("pptv", 'utf-8')
    message['Subject'] = Header('Python SMTP 邮件测试', 'utf-8')

    # 邮件正文内容
    message.attach(MIMEText('Python 邮件发送测试……', 'plain', 'utf-8'))

    # 构造附件1
    att1_path = '../data/pgc-cid.txt'
    att1 = MIMEText(open(att1_path, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="test.txt"'
    message.attach(att1)

    # 构造附件2
    att2_path = '../data/statistic_170616-170623.json'
    att2 = MIMEText(open(att2_path, 'rb').read(), 'base64', 'utf-8')
    att2["Content-Type"] = 'application/octet-stream'
    att2["Content-Disposition"] = 'attachment; filename="test.json"'
    message.attach(att2)

    try:
        # smtpObj = smtplib.SMTP(mail_host)
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)
        smtpObj.set_debuglevel(1)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        print "邮件发送成功"
    except smtplib.SMTPException, e:
        print "Error: 无法发送邮件,", e
