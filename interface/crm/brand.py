from common.send_method import SendMethod
from common.getKeyword_forResult import GetKeyword

class Brand:
    def __init__(self,url,method='post'):
        self.url = url
        self.method = method

    def pageBrandForViewList(self,data,headers):
        """
        :param data:
        :param headers:
        :return: 品牌列表
        """
        return SendMethod.send_method(self.method,url=self.url,json=data,headers=headers)

    def getByBrandName(self,data,headers):
        """

        :param data:
        :param headers:
        :return: 投放账号列表
        """
        # url = self.url + "?" + data
        # return SendMethod.send_method(method="get",url=url,headers=headers)
        return SendMethod.send_method(method="get",url=self.url,parmas=data,headers=headers)

    def get_keywords(self,res,keyword):
        """
        :param res:
        :param keyword:
        :return: key值的所有value
        """
        return GetKeyword.get_keywords(res,keyword)