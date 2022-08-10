import logging
import unittest
from interface.base.login import Login
from interface.crm.customer import Customer
from conf import config

logger = logging.getLogger("logger")

class Test_Customer_List(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.login = Login()
        cls.access_token = cls.login.get_access_token("xietao")
        cls.headers = {"Authorization": cls.access_token}
        try:
            cls.url = "{}/crm/customer/pageClientQueryList".format(config.testIP)
            cls.customer = Customer(cls.url)
            logger.info("=======【我的客户】查询客户测试开始=======")
        except Exception as e:
            logger.error(f"实例化Customer失败:{e}")
            raise e

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("=======【我的客户】查询客户测试结束=======")

    def test_search_customer_01(self):
        """查询个人公司"""
        data = {
            "type": 0,
            "owner": "1",
            "size": 20,
            "current": 1
        }
        try:
            res = self.customer.pageClientQueryList(data,self.headers)
            if len(res["data"]["records"]) != 0:
                types = self.customer.get_keywords(res,"type")
                for t in types:
                    assert (t == 0),"查询结果不是个人公司"
            logger.info("[测试通过]查询个人公司")
        except Exception as e:
            logger.error(f"[测试失败]查询个人公司{e}")
            raise e
