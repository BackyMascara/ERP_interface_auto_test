import datetime
import json
import logging
import unittest

from interface.organization.login import Login
from conf import config
from interface.crm.opportunity import Opportunity
from common import select_mysql

logger = logging.getLogger("logger")

class Test_Update_Opportunity(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.login = Login()
        cls.access_token = cls.login.get_access_token("xietao")
        cls.headers = {
            "Authorization":cls.access_token
        }
        try:
            cls.url = "{}/crm/Opportunity/".format(config.testIP)
            cls.opportunity = Opportunity(cls.url)
            logger.info("=======【商机管理】修改客户商机测试开始=======")
        except Exception as e:
            logger.error(f"实例化Oportunity失败:{e}")
            raise e

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("=======【商机管理】修改客户商机测试结束=======")

    def test_update_opportunity_01(self):
        """修改客户商机"""
        sql1 = "SELECT cr.id AS customerId,cp.`name` as companyName,cr.`name` AS customerName FROM `crm_customer` cr,`crm_company`cp WHERE cr.company_id=cp.id and username='xietao'"
        customer = select_mysql.select_records(sql1,0,config.crm)

        sql2 = "SELECT id FROM `crm_opportunity` WHERE username='xietao' AND deleted='N'"
        opy = select_mysql.select_records(sql2,0,config.crm)

        update_msg = {
            "opportunityName": "柯涯测试",
            "opportunityDetails":"学习自动化啦",
            "expectedSales":810,
            "expectedProfit":180,
            "orderedTime": str(datetime.date(2022,9,22)),
        }

        data = {
            "opportunityName":update_msg["opportunityName"],
            "companyName":customer[1],
            "customerName":customer[2],
            "customerId":customer[0],
            "opportunityDetails":update_msg["opportunityDetails"],
            "expectedSales":update_msg["expectedSales"],
            "expectedProfit":update_msg["expectedProfit"],
            "orderedTime":update_msg["orderedTime"],
            "id":opy[0]
        }
        url = self.url + str(opy[0])
        opportunity = Opportunity(url)
        try:
            res = opportunity.updateOpportunity(data,self.headers)
            assert ("处理成功" in res["msg"]),f"{res}"
            logger.info("[测试通过]修改客户商机")
        except Exception as e:
            logger.error(f"[测试失败]修改客户商机:{e}")
            raise e