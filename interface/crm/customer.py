import json
import random

from common.send_method import SendMethod
from common.getKeyword_forResult import GetKeyword
from conf import config
from interface.organization.login import Login

class Customer:
    def __init__(self,url = "{}/crm/customer/".format(config.testIP),method='post'):
        self.url = url
        self.method = method

    def customerUpdate(self,data,header):
        """
        修改客户
        :param data:
        :param header:
        :return:
        """
        return SendMethod.send_method(self.method,url=self.url,json=data,headers=header)

    def customerRegistration(self,data,header):
        """
        登记客户
        :param data:
        :param header:
        :return:
        """
        return SendMethod.send_method(self.method,url=self.url,json=data,headers=header)

    def pageClientQueryList(self,data,header):
        """
        查询公司（分页）
        :param data:
        :param header:
        :return:
        """
        return SendMethod.send_method(self.method,url=self.url,json=data,headers=header)

    def addPublic(self,header):
        """
        将客户抛入公海
        :param data:
        :param header:
        :return:
        """
        return SendMethod.send_method(method="get",url=self.url,headers=header)

    def companyProtect(self,data,header):
        """
        申请客户保护
        :param data:
        :param header:
        :return:
        """
        return SendMethod.send_method(self.method,url=self.url,json=data,headers=header)

    def add_invoice(self,data,header):
        """
        新增客户开票信息
        :param data:
        :param header:
        :return:
        """
        return SendMethod.send_method(self.method,url=self.url,json=data,headers=header)

    def update_invoice(self,data,header):
        """
        修改客户开票信息
        :param data:
        :param header:
        :return:
        """
        return SendMethod.send_method(method="put",url=self.url,json=data,headers=header)

    def get_keywords(self,res,keyword):
        """
        获取关键字的所有值
        :param res:
        :param keyword:
        :return:
        """
        return GetKeyword.get_keywords(res,keyword)

if __name__ == '__main__':
    login = Login()
    access_token = login.get_access_token("xietao")
    header = {"Authorization": access_token}
    url = "{}/crm/customer/pageClientQueryList".format(config.testIP)
    customer = Customer(url)
    # data = {"owner":"1","size":20,"current":1}
    data = {
        "type": 0,
        "owner":"1",
        "size": 20,
        "current": 1
    }
    res = customer.pageClientQueryList(data,header)

