import os,unittest,shutil,sys
from common import HTMLTestReportCN
from common.log_utils import logger
from common.email_utils import EmailUtils

current_path = os.path.dirname(__file__)
# print(current_path)
case_path = os.path.join(current_path,'testcases')
# print(case_path)
html_report_path = os.path.join(current_path,'html_reports/')
# print(html_report_path)
logger.info('测试用例开始执行')
discover_cases = None

try:
    discover_cases = unittest.defaultTestLoader.discover(start_dir=case_path,pattern='test*.py')
except ImportError as e:
    logger.error('测试用例路径配置错误，导致不能加载测试用例')
unite = unittest.TestSuite()
if discover_cases:
    unite.addTest(discover_cases)
    logger.info('加载测试用例到测试套件成功')
else:
    logger.error('加载测试用例到测试套件失败')


#创建测试报告路径对象
html_report_path_obj = HTMLTestReportCN.ReportDirectory(html_report_path)
html_report_path_obj.create_dir('WX_API_TEST')
#获取测试报告网页文件路径
html_report_file_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')
html_report_file_obj = open(html_report_file_path,'wb')
runner = HTMLTestReportCN.HTMLTestRunner(stream=html_report_file_obj,tester='P5工程师',title='微信测试项目',description='测试实战')
runner.run(unite)

email_body = '''
<h1 align = "center"> 接口自动化测试报告 </h1>
<p align = "center"> 详情见附件 </p>
'''
shutil.copyfile(html_report_file_path,'%s/WX_API_TEST.html'%sys.argv[1])
# EmailUtils(email_body, html_report_file_path).send_email()