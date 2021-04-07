import smtplib,os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailUtils:
    def __init__(self,email_body,email_attch_path=None):
        self.smtp_server = 'smtp.163.com'
        self.sender = 'featherwit96@163.com'
        self.password = 'IWNGJSPZVHVTLTIY'
        self.receiver = 'zhuhongchang@pekon.com,12111@121.com'
        self.cc = '991932716@qq.com,99997474@11.com'
        self.subject = 'P5P6接口自动化测试报告'
        self.body = email_body
        self.attch_path = email_attch_path

    def email_body(self):
        email_obj = MIMEMultipart()
        email_obj['from'] = self.sender
        email_obj['to'] = self.receiver
        email_obj['Cc'] = self.cc
        email_obj['subject'] = self.subject
        email_obj.attach( MIMEText(self.body,'html','utf-8') )
        if self.attch_path:
            attach_file = MIMEText(open(self.attch_path, 'rb').read(), 'base64', 'utf-8')
            attach_file['Content-type'] = 'application/octet-stream'
            attach_file.add_header('Content-Disposition','attachment',filename=('gbk','',os.path.basename(self.attch_path)) )
            email_obj.attach( attach_file )
        return email_obj

    def send_email(self):
        smtp = smtplib.SMTP()
        smtp.connect( self.smtp_server )
        smtp.login( user=self.sender,password=self.password )
        smtp.sendmail( self.sender, self.receiver.split(",")+self.cc.split(","),self.email_body().as_string())
        smtp.close()

if __name__ == '__main__':
    email_body = '''
    <h1 align="center"> 接口自动化测试报告  </h1>
    <p align="center"> 详情见附件 备注：封装后的 </p >
    '''
    html_file_path = os.path.join(os.path.dirname(__file__), '..', 'html_reports', 'WX_API_TESTV1.1',
                                      'WX_API_TESTV1.1.html')
    EmailUtils(email_body,html_file_path).send_email()