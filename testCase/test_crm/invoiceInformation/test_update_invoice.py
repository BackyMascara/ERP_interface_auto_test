import logging
import unittest
from interface.organization.login import Login
from interface.crm.customer import Customer
from conf import config
from common import select_mysql

logger = logging.getLogger("logger")

class Test_Update_Invoice(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.login = Login()
        cls.access_token = cls.login.get_access_token("xietao")
        cls.headers = {
            "Authorization": cls.access_token
        }
        try:
            cls.url = "{}/crm/invoiceInformation/".format(config.testIP)
            cls.customer = Customer(cls.url)
            logger.info("=======【我的客户】修改开票信息测试开始=======")
        except Exception as e:
            logger.error(f"实例化Customer失败:{e}")
            raise e

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("=======【我的客户】修改开票信息测试开始=======")

    def test_update_invoice_01(self):
        """修改客户开票信息"""
        sql = "SELECT cc.id as customerId FROM `crm_invoice_information` cii,`crm_customer` cc WHERE cii.customer_id=cc.id AND username='xietao'"
        customerId = select_mysql.select_records(sql,0,config.crm)[0]
        url = self.url + str(customerId)
        customer = Customer(url)
        print(customerId)
        data = {
            "taxNumber":"123456789012345678",
            "companyAddress":"python自动化",
            "companyPhone":"0795-1234566",
            "bankName":"建设伊娜很难过",
            "bankAccount":"6217002020062123427"
        }
        try:
            res = customer.update_invoice(data,self.headers)
            assert ("处理成功" in res["msg"]),f"{res}"
            logger.info("[测试通过]修改客户开票信息")
        except Exception as e:
            logger.error(f"[测试失败]修改客户开票信息{e}")
            raise e