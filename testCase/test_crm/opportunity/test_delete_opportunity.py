import logging
import unittest

from interface.base.login import Login
from interface.crm.opportunity import Opportunity
from conf import config
from common import select_mysql

logger = logging.getLogger("logger")

class Test_Delete_Opportunity(unittest.TestCase):
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
            logger.info("=======【商机管理】删除客户商机测试开始=======")
        except Exception as e:
            logger.error(f"实例化Oportunity失败:{e}")
            raise e

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("=======【商机管理】删除客户商机测试结束=======")

    def test_delete_opportunity_01(self):
        """删除客户商机"""
        sql = "SELECT id FROM `crm_opportunity` WHERE username='xietao' AND deleted='N'"
        res = select_mysql.select_records(sql,0,config.crm)
        url = self.url + str(res[0])
        opportunity = Opportunity(url)

        try:
            res = opportunity.deleteOpportunity(self.headers)
            assert (200 == res),f"{res}"
            logger.info("[测试通过]删除客户商机")
        except Exception as e:
            logger.error(f"[测试失败]删除客户商机:{e}")
            raise e