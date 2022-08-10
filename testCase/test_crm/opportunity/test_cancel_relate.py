import logging
import unittest

from interface.base.login import Login
from interface.crm.opportunity import Opportunity
from conf import config
from common import select_mysql

logger = logging.getLogger("logger")

class Test_Cancel_Relate(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.login = Login()
        cls.access_token = cls.login.get_access_token("xietao")
        cls.headers = {
            "Authorization": cls.access_token
        }
        try:
            cls.url = "{}/crm/Opportunity/cancelRelate/".format(config.testIP)
            cls.oppportunity = Opportunity(cls.url)
            logger.info("=======【商机管理】取消关联商机测试开始=======")
        except Exception as e:
            logger.error(f"实例化Opportunity失败{e}")
            raise e

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("=======【商机管理】取消关联商机测试结束=======")

    def test_cancel_relate_01(self):
        """取消关联商机"""
        sql = "SELECT id FROM `crm_opportunity` WHERE username='xietao' AND deleted='N'"
        res = select_mysql.select_records(sql,0,config.crm)
        url = self.url + str(res[0])
        oppportunity = Opportunity(url)
        try:
            res = oppportunity.cancelRelate(self.headers)
            assert ("处理成功" in res["msg"]), f"{res}"
            logger.info("[测试通过]取消关联商机")
        except Exception as e:
            logger.error(f"[测试失败]取消关联商机:{e}")
            raise e