import logging
import unittest
from interface.base.login import Login
from interface.crm.customer import Customer
from conf import config
from common import select_mysql

logger = logging.getLogger("logger")

class Test_Company_Protect(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.login = Login()
        cls.access_token = cls.login.get_access_token()
        cls.headers = {"Authorization": cls.access_token}
        try:
            cls.url = "{}/crm/companyProtect".format(config.testIP)
            cls.customer = Customer(cls.url)
            logger.info("=======【我的客户】客户保护测试开始=======")
        except Exception as e:
            logger.error(f"实例化Customer失败:{e}")
            raise e

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("=======【我的客户】客户保护测试结束=======")

    def test_company_protect_01(self):
        """申请客户保护"""
        sql = "SELECT c1.id as customerId,c1.`name` FROM `crm_company` c1,crm_customer c2 WHERE c2.company_id = c1.id AND type='1' AND c1.audit_flag='0' AND c2.protect_level='1' and username = 'xietao'"
        companyId = select_mysql.select_records(sql,0,config.crm)[0]
        companyName = select_mysql.select_records(sql,0,config.crm)[1]
        print(f"companyId:{companyId},公司名称:{companyName}")
        data = {
            "protectLevel":2,
            "companyName":companyName,
            "companyId":companyId,
            "state":2
        }
        try:
            res = self.customer.companyProtect(data,self.headers)
            print(res)
            assert ("处理成功" in res["msg"] or "保护中" in res["msg"]),f"{res}"
            logger.info("[测试通过]申请客户保护")
        except Exception as e:
            logger.error(f"[测试失败]申请客户保护{e}")
            raise e