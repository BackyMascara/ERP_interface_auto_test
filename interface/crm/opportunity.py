from common.getKeyword_forResult import GetKeyword
from common.send_method import SendMethod

class Opportunity:
    def __init__(self,url,method='post'):
        self.url = url
        self.method = method

    def pageOpportunityList(self,data,headers):
        """
        客户商机列表
        :param data:
        :param headers:
        :return:
        """
        return SendMethod.send_method(method="get",url=self.url,parmas=data,headers=headers)

    def saveOpportunity(self,data,headers):
        """
        新增客户商机
        :param data:
        :param headers:
        :return:
        """
        return SendMethod.send_method(self.method,url=self.url,json=data,headers=headers)

    def createRelate(self,headers):
        """
        添加关联商机
        :param data:
        :param headers:
        :return:
        """
        return SendMethod.send_method("put",url=self.url,headers=headers)

    def cancelRelate(self,headers):
        """
        取消关联商机
        :param data:
        :param headers:
        :return:
        """
        return SendMethod.send_method("put",url=self.url,headers=headers)

    def deleteOpportunity(self,headers):
        """
        删除客户商机
        :param headers:
        :return:
        """
        return SendMethod.send_method("delete",url=self.url,headers=headers)

    def updateOpportunity(self,data,headers):
        """
        修改客户商机
        :param data:
        :param headers:
        :return:
        """
        return SendMethod.send_method("put",url=self.url,json=data,headers=headers)

    def get_keywords(self,res,keyword):
        """
        获取res中key值的value
        :param res: 接口响应内容
        :param keyword: 关键字
        :return: 关键字的值
        """
        return GetKeyword.get_keywords(res,keyword)