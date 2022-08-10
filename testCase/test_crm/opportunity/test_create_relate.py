import logging
import unittest

from interface.base.login import Login
from conf import config
from interface.crm.opportunity import Opportunity
from common import select_mysql

logger = logging.getLogger("logger")

class Test_Create_Relate(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.login = Login()
        cls.access_token = cls.login.get_access_token("xietao")
        cls.headers = {
            "Authorization":cls.access_token
        }
        try:
            cls.url = "{}/crm/Opportunity/createRelate/".format(config.testIP)
            cls.oppportunity = Opportunity(cls.url)
            logger.info("=======【商机管理】添加关联商机测试开始=======")
        except Exception as e:
            logger.error(f"实例化Opportunity失败{e}")
            raise e

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("=======【商机管理】添加关联商机测试结束=======")

    def test_create_relate_01(self):
        """添加关联商机"""
        sql = "SELECT co.id AS opportunityId,customer_id FROM `crm_opportunity` co,`crm_customer` cc WHERE co.customer_id=cc.id AND cc.username='xietao'"
        res = select_mysql.select_records(sql,0,config.crm)
        url = self.url + str(res[0]) + "/" + str(res[1])
        oppportunity = Opportunity(url)
        try:
            res = oppportunity.createRelate(self.headers)
            assert ("处理成功" in res["msg"]),f"{res}"
            logger.info("[测试通过]添加关联商机")
        except Exception as e:
            logger.error(f"[测试失败]添加关联商机:{e}")
            raise e
