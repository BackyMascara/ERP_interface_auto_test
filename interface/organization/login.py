import logging

from common.send_method import SendMethod
from common.getKeyword_forResult import GetKeyword
from conf import config

logger = logging.getLogger('logger')

class Login:

    # url和请求方式对于一个接口来说是固定的，
    # 所以这两个参数可以写在初始化方法中。
    def __init__(self,url='{}/organization/login/sms_code'.format(config.testIP),method='post'):
        self.method = method
        self.url = url

    def login(self,data):
        return SendMethod.send_method(self.method,url=self.url,json=data)

    def get_keyword(self,res,keyword):
        """

        :param res:
        :param keyword:
        :return: key值的所有value
        """
        return GetKeyword.get_keyword(res,keyword)

    def get_access_token(self,username):
        """
        获得鉴权
        :return: access_token
        """
        data = {
            "username": username,
            "password": "a123456",
            "verificationCode": "悠悠"
        }
        try:
            res = SendMethod.send_method(method=self.method,url=self.url,json=data)
            assert (res['code'] == '200'),f"{res}"
            return res['data']['access_token']
        except Exception as e:
            raise e

if __name__ == '__main__':
    login = Login()
    login.get_access_token("xietao")
