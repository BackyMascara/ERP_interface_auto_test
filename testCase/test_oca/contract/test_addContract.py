import logging
import unittest
from interface.organization.login import Login
from conf import config
from interface.oca.contract import Contract
from common import select_mysql

logger = logging.getLogger("logger")

class Test_Add_Contract(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.login = Login()
        cls.access_token = cls.login.get_access_token("xietao")
        cls.headers = {"Authorization": cls.access_token}
        try:
            cls.url = "{}/oca/contract/addContract".format(config.testIP)
            cls.contract = Contract(cls.url)
            logger.info("=======【我的合同】新增合同测试开始=======")
        except Exception as e:
            logger.error(f"实例化Contract失败:{e}")
            raise e

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("=======【我的合同】新增合同测试结束=======")

    def test_add_contract_01(self):
        """新增合同类型：销售合同/合同"""
        sql = "SELECT cp.id as companyId,cp.`name` as companyName,cr.`name` AS customerName,cr.id AS customerId FROM `crm_customer` cr,`crm_company`cp WHERE cr.company_id=cp.id and username='xietao'"
        res = select_mysql.select_records(sql,0,config.crm)
        print(res)
        data = {
            "type":"01",
            "orderType":1,
            "contractAmount":"3000000",
            "taxPoint":"6",
            "feeTax":"众灿",
            "companyId":res[0],
            "companyName":res[1],
            "customerName":res[2],
            "customerId":res[3],
            "brand":"Cille希乐",
            "itemName":"保温杯品类合作项目",
            "estimateCost":"1400000",
            "estimateCustomerServiceFee":"300000",
            "estimateCustomerServicePercentage":0.1,
            "proportionType":1,
            "prepaid":"3000000",
            "contractTime":"2022-11-11",
            "implementRequire":"这是执行要求",
            "customerRefundType":2,
            "isYearContract":"2",
            "contractFileName":"[\"众灿互动服务合同.pdf\"]",
            "contractFileLink":"[\"https://zhogncan.oss-cn-beijing.aliyuncs.com/upfiles/erp/file/1667635243472-众灿互动服务合同.pdf\"]",
            "customerRefundFileName":"[\"标准合同-预览内容要正确显示_20210928173520.pdf\"]",
            "customerRefundFileLink":"[\"https://zhogncan.oss-cn-beijing.aliyuncs.com/upfiles/erp/file/1667635243985-标准合同-预览内容要正确显示_20210928173520.pdf\"]",
            "feeTaxId":628
        }
        try:
            res = self.contract.add_contract(data,self.headers)
            assert ("处理成功" in res["msg"]),f"{res}"
            logger.info("[测试通过]新增合同类型：销售合同/合同")
        except Exception as e:
            logger.error(f"[测试失败]新增合同类型：销售合同/合同:{e}")
            raise e

