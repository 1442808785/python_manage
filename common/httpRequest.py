import requests


s = requests.session()#创建一个会话

class HttpRequest:
    '''封装一个测试接口的工具'''
    def __init__(self,method,url,data):
        self.method = method
        self.url = url
        self.data = data

    def api_request(self,header = None):
        if self.method.lower() == 'get':
            res = s.get(self.url,params = self.data,headers = header,timeout=15)#json格式参数
            return res
        elif self.method.lower() == 'post':
            res = s.post(self.url,data = self.data,headers = header,timeout = 15)#form格式参数
            return res