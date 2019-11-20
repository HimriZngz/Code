import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'from@runoob.com'
receivers = ['yingqi1561@qq.com']

msg = MIMEText('Are you OK?', 'plain', 'utf-8')
msg['From'] = Header('菜鸟', 'utf-8')
msg['To'] = Header('测试', 'utf-8')

subject = 'Python SMTP 邮件'
msg['Subject'] = Header(subject, 'utf-8')


try:
    smtpobj = smtplib.SMTP('localhost')
    smtpobj.sendmail(sender, receivers, msg.as_string())
    print('发送成功')
except smtplib.SMTPException:
    print('发送失败')