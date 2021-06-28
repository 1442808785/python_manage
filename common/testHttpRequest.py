import unittest
from common.httpRequest import HttpRequest
from common.getExcel import DoExcel
from common.getData import GetTok
from common.getLogging import GetLog
from ddt import ddt,data
from common.readConfig import ReadConfig
import warnings


test_excel = DoExcel().read_excel()
@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        '''调用忽略warning函数，去除无所谓的警告'''

    @data(*test_excel)
    def test_api_request(self,item):
        GetLog().info('第{0}条用例:module是{1}，title是{2}'.format(item['id'],item['module'],item['title']))
        dir_url = eval(ReadConfig().read_config('URL', 'sys_ys'))
        res = HttpRequest(item['method'],dir_url+item['url'],eval(item['data'])).api_request()
        GetLog().info(res.json())
        try:
            self.assertEqual(item['expected'],res.json()['rtnCode'])
            msg = 'Pass'
        except AssertionError as e:
            msg = 'Fail'
            GetLog().error('出错原因是{}'.format(e))
            raise e#抛出错误
        finally:
            DoExcel().wirt_back(item['sheet_name'],item['id']+1,str(res.json()),msg)

    def tearDown(self):
        pass

if __name__ == '__main__':
    pass

    data = {"openid":"oqK5d5Z2lD_y_0o-I_-XC4rILlWs","pagesize":10,"state":-1,"page":1}