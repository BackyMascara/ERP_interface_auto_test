import logging
import unittest

from interface.base.login import Login
from conf import config

logger = logging.getLogger('logger')

class Test_login(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        try:
            #实例化Login类
            cls.url = "{}/organization/login/sms_code".format(config.testIP)
            cls.login = Login(cls.url)
            logger.info('=======【用户登录】测试开始=======')
        except Exception as e:
            logger.error(f'实例化Login失败:{e}')
            raise e

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info('=======【用户登录】测试结束=======')

    def test_login_01(self):
        '''账号、密码正确'''
        data = {
            "username":"fengyuxin",
            "password":"a123456",
            "verificationCode":"111"
        }
        try:
            res = self.login.login(data)
            print(res)
            assert('处理成功' in res['msg']),"登录失败"
            logger.info('[测试通过]账号、密码正确，登录成功')
        except Exception as e:
            print(e)
            logger.error(f'[测试失败]账号、密码正确，登录成功:{e}')
            raise e

    def test_login_02(self):
        '''账号正确、密码错误'''
        data = {
            "username": "wuchen",
            "password": "a",
            "verificationCode": "111"
        }
        try:
            res = self.login.login(data)
            assert ('用户名或密码错误！' in res['msg']),"提示信息错误"
            logger.info('[测试通过]账号正确、密码错误，登录失败')
        except Exception as e:
            logger.error(f'[测试失败]账号正确、密码错误，登录失败:{e}')
            raise e

    def test_login_03(self):
        '''账号错误、密码正确'''
        data = {
            "username": "w1",
            "password": "a123456",
            "verificationCode": "111"
        }
        try:
            res = self.login.login(data)
            assert ('用户名或密码错误！' in res['msg']),"提示信息错误"
            logger.info('[测试通过]账号错误、密码正确，登录失败')
        except Exception as e:
            logger.error(f'[测试失败]账号错误、密码正确，登录失败:{e}')
            raise e

if __name__ == '__main__':
    unittest.main()