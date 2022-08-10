import logging
import random
import unittest
from interface.base.login import Login
from conf import config
from interface.crm.customer import Customer
from common import getMobile

logger = logging.getLogger("logger")

class Test_Customer_Registration(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.login = Login()
        cls.access_token = cls.login.get_access_token()
        cls.header = {"Authorization": cls.access_token}
        try:
            cls.url = "{}/crm/customer/customerRegistration".format(config.testIP)
            cls.customer = Customer(cls.url)
            logger.info("=======【我的客户】新增客户测试开始=======")
        except Exception as e:
            logger.error(f"实例化Customer失败:{e}")
            raise e

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("=======【我的客户】新增客户测试结束=======")

    def test_add_customer_01(self):
        """新增企业客户：公司名、手机号重复，不能新增"""
        data = {
            "type":1,
            "companyName":"柯涯测试新增企业客户",
            "customerName":"柯涯",
            "mobile":"18456313213",
            "intentionLevel":"C",
            "wechat":"wx20220804",
            "email":"20220804@qq.com",
            "industry":"游戏",
            "brand":"众灿",
            "typeName":"甲方",
            "source":"熟人介绍",
            "associatedCustomersId":25882,
            "area":"海南藏族自治州",
            "remarks":"这是一条备注信息",
            "isStandardize":"false",
            "isNormalize":"true"
        }
        try:
            res = self.customer.customerRegistration(data,self.header)
            assert ("占用" in res["msg"]),f"{res}"
            logger.info("[测试通过]新增企业客户：公司名、手机号重复，不能新增")
        except Exception as e:
            logger.error(f"[测试失败]新增企业客户：公司名、手机号重复，不能新增:{e}")
            raise e

    def test_add_customer_02(self):
        """新增企业客户：公司名重复、手机号不重复，可以新增"""
        mobile = getMobile.get_mobile()
        data = {
            "type":1,
            "companyName":"柯涯测试新增企业客户",
            "customerName":"柯涯",
            "mobile":mobile,
            "intentionLevel":chr(random.randint(65,68)),
            "wechat":"wx" + mobile,
            "email":mobile + "@qq.com",
            "industry":"游戏",
            "brand":"众灿",
            "typeName":"甲方",
            "source":"熟人介绍",
            "associatedCustomersId":25882,
            "area":"海南藏族自治州",
            "remarks":"这是一条备注信息",
            "isStandardize":"false",
            "isNormalize":"true"
        }
        try:
            res = self.customer.customerRegistration(data,self.header)
            assert ("处理成功" in res["msg"]),f"{res}"
            logger.info("[测试通过]新增企业客户：公司名重复、手机号不重复，可以新增")
        except Exception as e:
            logger.error(f"[测试失败]新增企业客户：公司名重复、手机号不重复，可以新增:{e}")
            raise e

    def test_add_customer_03(self):
        """新增企业客户：公司名不重复、手机号重复，可以新增"""
        data = {
            "type": 1,
            "companyName": "柯涯测试新增企业客户" + str(random.randint(0,100)),
            "customerName": "柯涯",
            "mobile": "18456313213",
            "intentionLevel": chr(random.randint(65, 68)),
            "wechat": "wx18456313213",
            "email": "18456313213@qq.com",
            "industry": "游戏",
            "brand": "众灿",
            "typeName": "甲方",
            "source": "熟人介绍",
            "associatedCustomersId": 25882,
            "area": "海南藏族自治州",
            "remarks": "这是一条备注信息",
            "isStandardize": "false",
            "isNormalize": "true"
        }
        try:
            res = self.customer.customerRegistration(data, self.header)
            assert ("处理成功" in res["msg"]),f"{res}"
            logger.info("[测试通过]新增企业客户：公司名不重复、手机号重复，可以新增")
        except Exception as e:
            logger.error(f"[测试失败]新增企业客户：公司名不重复、手机号重复，可以新增:{e}")
            raise e

    def test_add_customer_04(self):
        """新增个人客户：手机号重复，不能新增"""
        data = {
            "type":0,
            "companyName":"个人",
            "customerName":"柯涯测试",
            "mobile":"13868953613",
            "intentionLevel":"B",
            "wechat":"wx13868953613",
            "email":"13868953613@qq.com",
            "industry":"运动户外",
            "brand":"iPhone",
            "typeName":"甲方",
            "source":"地推",
            "associatedCustomersId":25872,
            "area":"海外",
            "remarks":"这是备注",
            "isStandardize":"false",
            "isNormalize":"true"
        }
        try:
            res = self.customer.customerRegistration(data,self.header)
            assert ("占用" in res["msg"]),f"{res}"
            logger.info("[测试通过]新增个人客户：手机号重复，不能新增")
        except Exception as e:
            logger.error(f"[测试失败]新增个人客户：手机号重复，不能新增:{e}")
            raise e

    def test_add_customer_05(self):
        """新增个人客户：手机号不重复，可以新增"""
        mobile = getMobile.get_mobile()
        data = {
            "type": 0,
            "companyName": "个人",
            "customerName": "柯涯测试" + str(random.randint(0,100)),
            "mobile": mobile,
            "intentionLevel": chr(random.randint(65, 68)),
            "wechat": "wx" + mobile,
            "email": mobile + "@qq.com",
            "industry": "运动户外",
            "brand": "iPhone",
            "typeName": "甲方",
            "source": "地推",
            "associatedCustomersId": 25872,
            "area": "海外",
            "remarks": "这是备注",
            "isStandardize": "false",
            "isNormalize": "true"
        }
        try:
            res = self.customer.customerRegistration(data, self.header)
            assert ("处理成功" in res["msg"]),f"{res}"
            logger.info("[测试通过]新增个人客户：手机号不重复，可以新增")
        except Exception as e:
            logger.error(f"[测试失败]新增个人客户：手机号不重复，可以新增:{e}")
            raise e

    def test_add_customer_06(self):
        """新增个人客户：不填写手机号，不能新增"""
        data = {
            "type":0,
            "companyName":"个人",
            "customerName":"柯涯测试",
            "mobile":None,
            "intentionLevel":"B",
            "wechat":"wx13868953613",
            "email":"13868953613@qq.com",
            "industry":"运动户外",
            "brand":"iPhone",
            "typeName":"甲方",
            "source":"地推",
            "associatedCustomersId":25872,
            "area":"海外",
            "remarks":"这是备注",
            "isStandardize":"false",
            "isNormalize":"true"
        }
        try:
            res = self.customer.customerRegistration(data,self.header)
            assert ("联系方式不能为空" in res["data"]),f"{res}"
            logger.info("[测试通过]新增个人客户：不填写手机号，不能新增")
        except Exception as e:
            logger.error(f"[测试失败]新增个人客户：不填写手机号，不能新增:{e}")
            raise e

if __name__ == '__main__':
    unittest.main()