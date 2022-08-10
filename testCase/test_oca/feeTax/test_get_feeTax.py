import logging
import unittest

from interface.base.login import Login
from conf import config
from interface.oca.feeTax import FeeTax
from common import select_mysql

logger = logging.getLogger("logger")

class Test_Get_FeeTax(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.login = Login()
        cls.access_token = cls.login.get_access_token("yousuhong")
        cls.headers = {
            "Authorization":cls.access_token
        }
        try:
            cls.url = "{}/oca/feeTax/".format(config.testIP)
            cls.feeTax = FeeTax(cls.url)
            logger.info("=======【我方公司】我方公司详情测试开始=======")
        except Exception as e:
            logger.error(f"实例化FeeTax失败:{e}")
            raise e

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("=======【我方公司】我方公司详情测试结束=======")

    def test_get_feeTax_01(self):
        """通过id查询抬头详情"""
        sql = "SELECT id FROM `t_fee_tax`"
        ftId = select_mysql.select_records(sql,0,config.oca)[0]
        url = self.url + str(ftId)
        feeTax = FeeTax(url)
        try:
            res = feeTax.get_feeTax(self.headers)
            assert (res["data"]["id"] == ftId),f"{res}"
            logger.info("[测试通过]通过id查询抬头详情")
        except Exception as e:
            logger.error("[测试失败]通过id查询抬头详情")
            raise e