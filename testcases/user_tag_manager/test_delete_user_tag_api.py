import unittest,requests,jsonpath
from common import public_api_infos
class TestRequestsDemo(unittest.TestCase):#编写一个类，继承TestCase
    #fixture配置代码
    def setUp(self) -> None:
        # self.hosts = 'api.weixin.qq.com'
        self.session = requests.session()
    def tearDown(self) -> None:
        self.session.close()

    def test_01_delete_user_tag(self):
        self._testMethodName = 'VXC_YH_003'
        self._testMethodDoc = '验证不能删除标签id为0的标签'
        # url_params = {
        #     "grant_type": "client_credential",
        #     "appid": "wx351a03f64f7b147f",
        #     "secret": "d80a853d34c3fc7788a8cd9579302b84"
        # }
        # response = public_api_infos.get_access_token_api(self.session, url_params)
        # json_obj = response.json()
        # token_id = jsonpath.jsonpath(json_obj, '$.access_token')[0]
        token_id = public_api_infos.get_token(session=self.session)
        url_params = {
            "access_token": token_id
        }
        post_data = {"tag": {"id": 0}}
        response = public_api_infos.delete_user_tag_api(self.session, url_params, post_data)
        actual_result = jsonpath.jsonpath(response.json(),'$.errcode')[0]
        self.assertEqual(actual_result,45058,'[VXC_YH_003]用例执行失败')

if __name__ == '__main__':
    unittest.main(verbosity=2)