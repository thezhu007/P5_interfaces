# 方法一：
# class ConfigUtils:
#     @property
#     def Hosts(self): #方法变属性方法
#         return 'api.weixin.qq.com'
#
# config = ConfigUtils()
#
# if __name__ =='__main__':
#     print(config.Hosts)

#方法二：
import configparser,os
config_file_path = os.path.join(os.path.dirname(__file__),'..','conf','config.ini')
class ConfigUtils:
    def __init__(self,config_file = config_file_path):
        self.cfg_obj = configparser.ConfigParser()
        self.cfg_obj.read(config_file,encoding='utf-8')
    @property
    def Hosts(self):  # 方法变属性方法
        host_value = self.cfg_obj.get('default','HOSTS')
        return host_value

    @property
    def appid(self):  # 方法变属性方法
        appid_value = self.cfg_obj.get('user_info', 'appid')
        return appid_value

    @property
    def secret(self):  # 方法变属性方法
        secret_value = self.cfg_obj.get('user_info', 'secret')
        return secret_value

config = ConfigUtils()
if __name__ =='__main__':
    print(ConfigUtils().Hosts)
    print(ConfigUtils().appid)
    print(ConfigUtils().secret)
