import unittest,requests,json,jsonpath
from common import public_api_infos
class TestRequestsDemo(unittest.TestCase):#编写一个类，继承TestCase
    #fixture配置代码
    def setUp(self) -> None:
        # self.hosts = 'api.weixin.qq.com'
        self.session = requests.session()
    def tearDown(self) -> None:
        self.session.close()

    def test_01_create_user_tag(self):
        self._testMethodName = 'VXC_YH_001'
        self._testMethodDoc = '验证调用创建标签接口能否成功创建'
        url_params = {
            "grant_type": "client_credential",
            "appid": "wx351a03f64f7b147f",
            "secret": "d80a853d34c3fc7788a8cd9579302b84"
        }
        # response = self.session.get(url='https://%s/cgi-bin/token' % self.hosts, params=url_params)
        response = public_api_infos.get_access_token_api(self.session, url_params)
        json_obj = response.json()
        token_id = jsonpath.jsonpath(json_obj, '$.access_token')[0]
        url_params = {
            "access_token": token_id
        }
        post_data={"tag":{"name":"大学生8"}}
        post_data_str1 = json.dumps(post_data,ensure_ascii=False)
        # response = requests.post(url='https://%s/cgi-bin/tags/create'%self.hosts, params=url_params,
        #                             data=post_data_str1.encode('utf-8'))
        response = public_api_infos.creat_user_tag_api(self.session,url_params,post_data)
        actual_result = jsonpath.jsonpath(response.json(), '$.tag.name')[0]
        self.assertEqual(actual_result,'大学生8')

if __name__ == '__main__':
    unittest.main(verbosity=2)


