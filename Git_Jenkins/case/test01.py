# encoding: utf-8
"""
@author:Administrator
@file: test12.py
@time: 2018/08/{DAY}
"""

import unittest
import requests



class TestQQ(unittest.TestCase):

    def setUp(self):
        self.rqs = requests.session()
        self.url = 'http://japi.juhe.cn/qqevaluate/qq'

    def tearDown(self):
        self.rqs.close()

    def test01(self):
        '''用例1：错误的key'''

        par = {"key": "xxx",  # appkey需要注册申请
                "qq":  "283340479"
               }

        rq = self.rqs.get(self.url, params=par)
        text = eval(rq.text)

        # print("test01:%s" % text)
        # print(text['reason'])
        self.assertEqual(text['reason'],'KEY ERROR!')

    def test02(self):
        '''用例2：正确的key'''

        par = {"key": "8dbee1fcd8627fb6699bce7b986adc45",  # appkey需要注册申请
               "qq": "283340479"
               }

        rq = self.rqs.get(self.url, params=par)
        text = rq.text

        # print("test01:%s" % text)
        # print(rq.json())
        self.assertEqual(rq.json()['reason'], 'success')

    def test03(self):
        '''用例3：错误的qq'''

        par = {"key": "8dbee1fcd8627fb6699bce7b986adc45",  # appkey需要注册申请
               "qq": "2833xxxxx"
               }

        rq = self.rqs.get(self.url, params=par)
        text = rq.text

        # print("test01:%s" % text)
        # print(rq.json())
        self.assertEqual(rq.json()['reason'], '错误的请求参数')


if __name__ == "__main__":
    unittest.main()