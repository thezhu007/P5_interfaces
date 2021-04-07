import os,configparser
config_file_path = os.path.join(os.path.dirname(__file__),'..','conf','config.ini')
cfg_obj = configparser.ConfigParser()#创构建一个配置文件对象
cfg_obj.read(config_file_path)#配置文件对象加载配置文件
value = cfg_obj.get('path','CASE_PATH')
print(value)

#进行二次封装，更适应框架
