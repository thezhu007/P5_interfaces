import smtplib,os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
email_body = '''
<h1 align = "center"> 接口自动化测试报告 </h1>
<p align = "center"> 详情见附件 </p>
'''
html_file_path = os.path.join(os.path.dirname(__file__),'..','html_reports','WX_API_TESTV1.1','WX_API_TESTV1.1.html')

text_obj = MIMEText(email_body,'html','utf-8')

attach_file = MIMEText( open(html_file_path,'rb').read(),'base64','utf-8')
attach_file['Content-type'] = 'application/octet-stream'
attach_file.add_header('Content-Disposition','attachment',filename = ('gbk','','WX_API_TESTV1.1.html'))

email_obj = MIMEMultipart()
email_obj.attach(text_obj)
email_obj.attach(attach_file)
email_obj['from'] = 'featherwit96@163.com' #发件人
email_obj['to'] = 'zhuhongchang@pekon.com' #收件人
email_obj['Cc'] = '991932716@qq.com' #抄送人
email_obj['subject'] = 'P5自动化测试报告' #主题

smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')
#邮箱授权码
smtp.login(user='featherwit96@163.com',password='IWNGJSPZVHVTLTIY')
smtp.sendmail('featherwit96@163.com','zhuhongchang@pekon.com',email_obj.as_string())
smtp.close()
