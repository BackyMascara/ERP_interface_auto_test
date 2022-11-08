from common.send_method import SendMethod

class Contract:
    def __init__(self,url,methond="post"):
        self.url = url
        self.method = methond

    def add_contract(self,data,headers):
        """
        新增合同
        :param data:
        :param headers:
        :return:
        """
        return SendMethod.send_method(self.method,url=self.url,json=data,headers=headers)
