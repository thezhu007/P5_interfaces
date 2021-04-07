import logging
#相当于输出语句，默认输出error
# logging.info('info')
# logging.error('error')

log_obj = logging.getLogger('P5')#日志的名称
log_obj.setLevel(10)#设置日志的默认级别
handler1 = logging.StreamHandler()#创建handler对象，给日志进行级别、格式等配置的输出方式
handler1.setLevel(10)#设置handler对象日志等级，设置日志的打印级别，只打印当前级别和比他高的级别
handler2 = logging.FileHandler('./test.log','a',encoding = 'utf-8')
handler2.setLevel(20)
#创建一个日志格式对象
formatter = logging.Formatter('%(asctime)s__%(name)s__%(levelname)s__%(message)s')
#把日志格式配置到handler对象
handler1.setFormatter(formatter)
#核心 把handler对象设置加载到日志对象
log_obj.addHandler(handler1)
log_obj.addHandler(handler2)

log_obj.debug('debug')
log_obj.info('info')
log_obj.warning('warning')
log_obj.error('error')
log_obj.critical('critical')
