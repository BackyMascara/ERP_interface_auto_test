import logging
import unittest
from conf import config
from interface.base.login import Login
from interface.crm.customer import Customer
from common import select_mysql

logger = logging.getLogger("logger")

class Test_Customer_Update(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.login = Login()
        cls.access_token = cls.login.get_access_token("xietao")
        cls.headers = {"Authorization": cls.access_token}
        try:
            cls.url = "{}/crm/customer/".format(config.testIP)
            cls.customer = Customer(cls.url)
            logger.info("=======【我的客户】修改客户测试开始=======")
        except Exception as e:
            logger.info(f"实例化Customer失败:{e}")
            raise e

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("=======【我的客户】修改客户测试结束=======")

    def test_update_customer_01(self):
        """修改企业客户：公司名、手机号重复，不能修改"""
        sql = "SELECT c2.id as customerId FROM `crm_company` c1,crm_customer c2 WHERE c2.company_id = c1.id AND type='1' AND is_standardize='0'"
        customerId = select_mysql.select_records(sql,0,config.crm)[0] # 得到非标准的企业公司id
        url = self.url + str(customerId)
        customer = Customer(url)

        data = {
            "type":1,
            "companyName":"柯涯测试新增企业客户",
            "customerName":"柯涯",
            "mobile":"13259604012",
            "intentionLevel":"C",
            "wechat":"wx13259605017",
            "email":"13259605017@qq.com",
            "industry":"","brand":"众灿",
            "typeName":"甲",
            "source":"熟人介绍",
            "area":"",
            "remarks":"这是一条备注信息",
            "id":customerId,
            "isStandardize":"false",
            "isNormalize":"true"
        }
        try:
            res = customer.customerUpdate(data,self.headers)
            assert ("占用" in res["msg"]),f"{res}"
            logger.info("[测试通过]修改企业客户：公司名、手机号重复，不能修改")
        except Exception as e:
            logger.error("[测试失败]修改企业客户：公司名、手机号重复，不能修改")
            raise e

    def test_update_customer_02(self):
        """修改个人客户：手机号重复，不能修改"""
        sql = "SELECT c2.id as customerId FROM `crm_company` c1,crm_customer c2 WHERE c2.company_id = c1.id AND type='0' AND is_standardize='0'"
        customerId = select_mysql.select_records(sql,0,config.crm)[0] # 得到个人公司id
        url = self.url + str(customerId)
        customer = Customer(url)

        data = {
            "type":0,
            "companyName":"个人",
            "customerName":"柯涯测试",
            "mobile":"14325354345",
            "intentionLevel":"A",
            "wechat":"wx13259604927",
            "email":"13259604927@qq.com",
            "industry":"",
            "brand":"个人",
            "typeName":"",
            "source":"地推",
            "associatedCustomersId":25872,
            "area":"",
            "remarks":"这是备注",
            "id":customerId,
            "isStandardize":"false",
            "isNormalize":"true"
        }
        try:
            res = customer.customerUpdate(data,self.headers)
            assert ("占用" in res["msg"]),f"{res}"
            logger.info("[测试通过]修改企业客户：公司名、手机号重复，不能修改")
        except Exception as e:
            logger.error("[测试失败]修改企业客户：公司名、手机号重复，不能修改")
            raise e

    def test_update_customer_03(self):
        """将企业客户修改为个人客户，修改失败"""
        sql = "SELECT c2.id as customerId FROM `crm_company` c1,crm_customer c2 WHERE c2.company_id = c1.id AND type='1' AND is_standardize='0'"
        customerId = select_mysql.select_records(sql,0,config.crm)[0] # 得到非标准的企业公司id
        url = self.url + str(customerId)
        customer = Customer(url)

        data = {
            "type":0,
            "companyName":"个人",
            "customerName":"柯涯测试",
            "mobile":"13868953613",
            "intentionLevel":"B",
            "wechat":"wx13868953613",
            "email":"13868953613@qq.com",
            "id":customerId,
            "isStandardize":"false",
            "isNormalize":"true"
        }
        try:
            res = customer.customerUpdate(data,self.headers)
            assert ("企业不能更改为个人" in res["msg"]),f"{res}"
            logger.info("[测试通过]将企业客户修改为个人客户，修改失败")
        except Exception as e:
            logger.error(f"[测试失败]将企业客户修改为个人客户，修改失败{e}")
            raise e


if __name__ == '__main__':
    unittest.main()
