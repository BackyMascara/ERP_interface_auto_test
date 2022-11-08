from common.send_method import SendMethod

class Flow:
    def __init__(self,url,method="post"):
        self.url = url
        self.method = method

    def agreeProcess(self,headers):
        """
        流程审核通过
        :param data:
        :param headers:
        :return:
        """
        return SendMethod.send_method(self.method,self.url,headers=headers)

    def rejectProcess(self,headers):
        """
        流程审核驳回
        :param data:
        :param headers:
        :return:
        """
        return SendMethod.send_method(self.method,self.url,headers=headers)