import logging
import unittest
from interface.base.login import Login
from conf import config
from common import select_mysql
from interface.crm.opportunity import Opportunity

logger = logging.getLogger("logger")

class Test_Add_Opportunity(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.login = Login()
        cls.access_token = cls.login.get_access_token("xietao")
        cls.headers = {
            "Authorization":cls.access_token
        }
        try:
            cls.url = "{}/crm/Opportunity/saveOpportunity".format(config.testIP)
            cls.opportunity = Opportunity(cls.url)
            logger.info("=======【商机管理】新增商机测试开始=======")
        except Exception as e:
            logger.error(f"实例化Opportunity失败:{e}")
            raise e

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("=======【商机管理】新增商机测试结束=======")

    def test_add_opportunity_01(self):
        """新增客户商机"""
        sql = "SELECT cr.id AS customerId,cp.`name` as companyName,cr.`name` AS customerName FROM `crm_customer` cr,`crm_company`cp WHERE cr.company_id=cp.id and username='xietao'"
        res = select_mysql.select_records(sql,0,config.crm)
        print(res)
        data = {
            "opportunityName":"商机给",
            "companyName":res[1],
            "customerName":res[2],
            "customerId":res[0],
            "opportunityDetails":"哥",
            "expectedSales":1000,
            "expectedProfit":235,
            "orderedTime":"2022-08-24T08:38:43.231Z"
        }
        try:
            res = self.opportunity.saveOpportunity(data,self.headers)
            assert ("处理成功" in res["msg"]),f"{res}"
            logger.info("[测试通过]新增客户商机")
        except Exception as e:
            logger.error(f"[测试失败]新增客户商机{e}")
            raise e