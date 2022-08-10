import logging
import unittest
import urllib.parse

from interface.crm.opportunity import Opportunity
from interface.organization.login import Login
from conf import config
import requests

logger = logging.getLogger("logger")

class Test_Opportunity_List(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.login = Login()
        cls.access_token = cls.login.get_access_token("xietao")
        cls.headers = {"Authorization": cls.access_token}
        try:
            cls.url = "{}/crm/Opportunity/pageOpportunityList".format(config.testIP)
            cls.opportunity = Opportunity(cls.url)
            logger.info("=======【商机管理】商机列表测试开始=======")
        except Exception as e:
            logger.error(f"实例化Opportunity失败:{e}")
            raise e

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("=======【商机管理】商机列表测试结束=======")

    def test_opportunity_list_01(self):
        """组合查询商机列表"""
        opportunityName = "675"
        customerName = "吴"
        companyName = "上海"
        data = f"current=1&size=20&opportunityName={urllib.parse.quote(opportunityName)}&customerName={urllib.parse.quote(customerName)}&companyName={urllib.parse.quote(companyName)}&createdTimeStart=2022-05-01&createdTimeEnd=2022-05-31"
        try:
            res = self.opportunity.pageOpportunityList(data,self.headers)
            if len(res["data"]["records"]) != 0:
                opportunityNames = self.opportunity.get_keywords(res,"opportunityName")
                customerNames = self.opportunity.get_keywords(res,"customerName")
                companyNames = self.opportunity.get_keywords(res,"companyName")
                for o in opportunityNames:
                    assert (opportunityName in o),"商机名称不一致"
                for c in customerNames:
                    assert (customerName in c),"联系人名称不一致"
                for c in companyNames:
                    assert (companyName in c),"公司名称不一致"
            else:
                print("没有查询结果")
            logger.info("[测试通过]组合查询商机列表")
        except Exception as e:
            logger.error(f"[测试失败]组合查询商机列表{e}")
            raise e