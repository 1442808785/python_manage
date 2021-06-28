import unittest
import HTMLTestRunnerNew
from common.testHttpRequest import TestHttpRequest

suit = unittest.TestSuite()#创建一个存储器
loader = unittest.TestLoader()#创建一个加载器
suit.addTest(loader.loadTestsFromTestCase(TestHttpRequest))

with open('datareport/燕瘦小程序测试报告.html', 'wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title="燕瘦小程序测试报告",
                                              description="接口自动化测试",tester="秋")
    runner.run(suit)