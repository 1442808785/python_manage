import configparser
from common.getPath import conf_path

class ReadConfig:
    '''读取配置文件'''
    @staticmethod
    def read_config(section,option):
        conf = configparser.ConfigParser()
        conf.read(conf_path,encoding='UTF-8')
        red = conf.get(section,option)
        return red

# if __name__ == '__main__':
#     print(ReadConfig().read_config(conf_path,'MODULE','module'))