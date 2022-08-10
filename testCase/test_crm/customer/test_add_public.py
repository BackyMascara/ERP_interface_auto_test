import logging
import unittest
from interface.base.login import Login
from interface.crm.customer import Customer
from conf import config
from common import select_mysql

logger = logging.getLogger("logger")

class Test_Add_Public(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.login = Login()
        cls.access_token = cls.login.get_access_token("xietao")
        cls.headers = {"Authorization": cls.access_token}
        try:
            cls.url = "{}/crm/customer/addPublic/".format(config.testIP)
            cls. customer = Customer(cls.url)
            logger.info("=======【我的客户】抛入公海测试开始=======")
        except Exception as e:
            logger.error(f"实例化Customer失败:{e}")
            raise e

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("=======【我的客户】抛入公海测试结束=======")

    def test_add_public_01(self):
        """将客户抛入公海"""
        sql= "SELECT c2.id as customerId FROM `crm_company` c1,crm_customer c2 WHERE c2.company_id = c1.id AND c1.audit_flag='0' AND is_public='0' and c2.username = 'xietao'"
        customerId = select_mysql.select_records(sql,0,config.crm)[0]
        url = self.url + str(customerId)
        customer = Customer(url)

        try:
            res = customer.addPublic(self.headers)
            assert ("处理成功" in res["msg"]),f"{res}"
            logger.info("[测试通过]将客户抛入公海")
        except Exception as e:
            logger.error(f"[测试失败]将客户抛入公海{e}")
            raise e
