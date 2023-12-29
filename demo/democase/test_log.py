import logging

# logging.basicConfig(level=logging.ERROR)

# my_format = logging.Formatter('%(module)s-%(name)s-%(levelno)s')     ##logging.Formatter 提供字符串显示

'''设置日志记录格式'''
my_format = '%(module)s-%(name)s-%(levelno)s-%(levelname)s'
logging.basicConfig(
    format=my_format,
    level=logging.ERROR,
    filename='mylog'
)

logging.info('1')
logging.error('2')
logging.debug('3')
logging.critical('5')
logging.warning('4')