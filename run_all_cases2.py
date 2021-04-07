import unittest
import os
from common import HTMLTestReportCN

current_path = os.path.dirname(__file__)

case_path = os.path.join( current_path , 'testcases')
html_report_path = os.path.join( current_path , 'html_reports/')
# print(current_path,case_path,html_report_path)

discover_cases = unittest.defaultTestLoader.discover(start_dir=case_path,
                                                     pattern='test*.py')
api_case_suite = unittest.TestSuite()
api_case_suite.addTest( discover_cases )

# 创建测试报告路径对象
html_report_path_obj = HTMLTestReportCN.ReportDirectory( html_report_path )
html_report_path_obj.create_dir('WX_API_TEST_') # 创建测试报告路径
# 获取测试报告网页文件的路径
html_report_file_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')
html_report_file_obj = open( html_report_file_path ,'wb' )
runner = HTMLTestReportCN.HTMLTestRunner(stream=html_report_file_obj,
                                         tester='P5P6工程师们',
                                         title='微信公众平台接口测试项目',
                                         description='实战使用')
runner.run( api_case_suite )