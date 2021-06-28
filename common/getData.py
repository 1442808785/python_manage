import requests
from common.readConfig import ReadConfig
# import pandas as pd
# from common.getPath import file_path

dir_url = eval(ReadConfig().read_config('URL','sys_ys'))
class GetTok:
    @staticmethod
    def get_token():
        url = dir_url+'/findUserName'
        data = {"username":"admin","password":"jhadmin222999ii"}
        res = requests.post(url,data = data,headers = None)
        token = res.json()['msg']
        # print(res.json())
        return token


#客服系统数据：
# class GetTok:
#     @staticmethod
#     def get_token():
#         url = dir_url+'/auth/oauth/token'
#         data = {"client_id":"jh_customer","grant_type":"password","scope":"ROOT_ADMIN","client_secret":"jhcustomer123",
#                 "password":"guoqiujian","username":"guoqiujian"}
#         header = {"Content-Type":"application/json;charset=UTF-8"}
#         res = requests.post(url,data,header)
#         token = res.json()['access_token']
#         return token
#
#     @classmethod
#     def get_mimc(cls):
#         url = dir_url+'/system/v1/system/open/account/token'
#         data = {"appAccount":"klfdgldfgdfg"}
#         header = {"Content-Type": "application/json;charset=UTF-8","token":cls().get_token()}
#         datas = json.dumps(data)
#         res = requests.post(url,data = datas,headers = header)
#         mimc_token = res.json()['data']['token']
#         return mimc_token
#
# class GetHeader:
#     get_header = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"+GetTok().get_mimc(),"token":GetTok.get_token()}

if __name__ == '__main__':
    pass