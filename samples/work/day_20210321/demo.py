import logging

logger = logging.getLogger('work01')
logger.setLevel(10)
consloe_handler = logging.StreamHandler()

formatter = logging.Formatter('%(levelno)s__%(levelname)s__%(pathname)s__%(filename)s__%(funcName)s__%(lineno)s__%(asctime)s__%(thread)d__%(threadName)s__%(process)d__%(message)s')
consloe_handler.setFormatter(formatter)
logger.addHandler(consloe_handler)

logger.info('hello')