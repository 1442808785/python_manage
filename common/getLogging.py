import logging
from common.getPath import log_path
class GetLog:
    def get_log(self,level,msg):
        suit_logging = logging.getLogger()
        suit_logging.setLevel('DEBUG')
        '''创建存储'''

        file_log = logging.FileHandler(log_path,encoding='UTF-8')
        file_log.setLevel('DEBUG')
        load_logging = logging.StreamHandler()
        load_logging.setLevel('DEBUG')
        '''创建渠道'''

        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')
        file_log.setFormatter(formatter)
        load_logging.setFormatter(formatter)
        '''设置样式'''

        suit_logging.addHandler(file_log)
        suit_logging.addHandler(load_logging)
        '''对接渠道'''

        if level == 'DEBUG':
            logging.debug(msg)
        elif level == 'INFO':
            logging.info(msg)
        elif level == 'WARNING':
            logging.warning(msg)
        elif level == 'ERROR':
            logging.error(msg)
        elif level == 'CRITICAL':
            logging.critical(msg)

        suit_logging.removeHandler(file_log)
        suit_logging.removeHandler(load_logging)
        '''关闭输出渠道'''

    def debug(self,MSG):
        self.get_log('DEBUG',MSG)

    def info(self,MSG):
        self.get_log('INFO',MSG)

    def warning(self,MSG):
        self.get_log('WARNING',MSG)

    def error(self,MSG):
        self.get_log('ERROR',MSG)

    def critical(self,MSG):
        self.get_log('CRITICAL',MSG)

# if __name__ == '__main__':
#     GetLog().get_info('hahah')
#     GetLog().get_error('完了，错了')
