import os

base_path = os.path.split(os.path.split(__file__)[0])[0]
'''获取顶级目录'''

file_path = os.path.join(base_path,'testData/燕瘦小程序.xlsx')
'''获取文件目录'''

conf_path = os.path.join(base_path,'testData/test.config')
'''获取配置文件目录'''

log_path = os.path.join(base_path,'testData/log.txt')
'''获取日志文件目录'''

# print(conf_path)
# print(file_path)
# print(conf_path)
# print(log_path)
# print(base_path)