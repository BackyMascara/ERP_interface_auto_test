from common.send_method import SendMethod

class FeeTax:
    def __init__(self,url,method="post"):
        self.url = url
        self.method = method

    def get_feeTax(self,headers):
        """
        我方公司详情
        :param headers:
        :return:
        """
        return SendMethod.send_method("get",url=self.url,headers=headers)
