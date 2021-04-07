#如何使用unittest
import unittest,requests,json,jsonpath
from common import public_api_infos
class TestRequestsDemo(unittest.TestCase):#编写一个类，继承TestCase
    #fixture配置代码
    def setUp(self) -> None:
        # self.hosts = 'api.weixin.qq.com'
        self.session = requests.session()
        self.proxy_server = {"http":"http://127.0.0.1:8888"}
    def tearDown(self) -> None:
        self.session.close()

#默认测试用例执行顺序，字符串由小到大升序
    def test_02_get_token(self):#编写测试用例
        self.assertEqual(1,1)

    def test_01_get_token(self):#编写测试用例
        url_params = {
            "grant_type": "client_credential",
            "appid": "wx351a03f64f7b147f",
            "secret": "d80a853d34c3fc7788a8cd9579302b84"
        }
        response = public_api_infos.get_access_token_api(self.session,url_params)
        json_obj = response.json()
        actual_result = jsonpath.jsonpath(json_obj,'$.expires_in')[0]
        self.assertEqual(actual_result,7200)#断言语句


if __name__ == '__main__':
    # unittest.main(verbosity=2)
    #addTest
    suite = unittest.TestSuite()
    suite.addTest(TestRequestsDemo('test_02_get_token'))
    suite.addTest(TestRequestsDemo('test_01_get_token'))
    unittest.main(verbosity=2,defaultTest='suite')