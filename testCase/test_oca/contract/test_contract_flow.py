import logging
import time
import unittest
from common import select_mysql
from conf import config
from interface.organization.login import Login
from interface.base.flow import Flow

logger = logging.getLogger("logger")

class Test_Contract_Flow(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        logger.info("=======【我的合同】审批合同测试开始=======")

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("=======【我的合同】审批合同测试结束=======")

    def test_agree_contract(self):
        """合同审批通过"""
        #1.找到一个合同审核中的合同
        sql = "SELECT id,contract_num FROM `t_biz_contract` WHERE state=3 and created_by='xietao' ORDER BY id DESC"
        res = select_mysql.select_records(sql,0,config.oca)
        data_id = res[0]
        logger.info(f"合同审批通过时，编号为:{res[1]}")
        state = 3

        #2.如果合同的状态审核中，就一直审核
        while (state==3):
            #2.1找到当前的流程审核人
            res = self.get_flow(data_id)
            #2.2审批通过
            self.agree_flow(res[0],data_id,res[1])
            #2.3获取当前合同的状态
            sql = f"SELECT state FROM `t_biz_contract` WHERE id={data_id}"
            res = select_mysql.select_records(sql,0,config.oca)
            state = res[0]

            time.sleep(3) # 避免短时间内频繁审批
        logger.info("[测试通过]审批通过合同")

    def test_reject_contract(self):
        """合同审批驳回"""
        sql = "SELECT id,contract_num FROM `t_biz_contract` WHERE state=3 and created_by='xietao'"
        res = select_mysql.select_records(sql,0,config.oca)
        data_id = res[0]
        logger.info(f"合同审批驳回时，编号为:{res[1]}")
        res = self.get_flow(data_id)
        res = self.reject_flow(res[0],data_id,res[1])

    def get_flow(self,data_id):
        """
        找到流程审核人、流程号
        :param data_id: 合同id
        :return: username,model_flag
        """
        sql = f"SELECT user_name,model_flag FROM `flow_business_map` WHERE data_id={data_id}"
        res = select_mysql.select_records(sql, 0, config.base)
        name, model_flag = res[0], res[1]
        logger.info(f"审核人:{name}[流程号:{model_flag}]")
        sql = f"SELECT username FROM `sys_user` where name='{name}'"
        res = select_mysql.select_records(sql, 0, config.org)
        username = res[0]
        return username,model_flag

    def agree_flow(self,username,dataId,modelFlag):
        """
        用于审批通过
        :param username:
        :param dataId: 合同id
        :param modelFlag: 流程模块标识
        :return:
        """
        login = Login()
        access_token = login.get_access_token(username)
        headers = {"Authorization":access_token}
        try:
            url = "{}/base/flow/agreeProcess?dataId={}&modelFlag={}".format(config.testIP,dataId,modelFlag)
            flow = Flow(url)
            res = flow.agreeProcess(headers)
            assert ("处理成功" in res['msg']),f"{res}"
        except Exception as e:
            logger.error(f"[测试失败]审批通过合同:{e}")
            raise e

    def reject_flow(self, username, dataId, modelFlag):
        """
        用于审批驳回
        :param username:
        :param dataId: 合同id
        :param modelFlag: 流程模块标识
        :return:
        """
        login = Login()
        access_token = login.get_access_token(username)
        headers = {"Authorization": access_token}
        try:
            url = "{}/base/flow/rejectProcess?dataId={}&modelFlag={}".format(config.testIP, dataId, modelFlag)
            flow = Flow(url)
            res = flow.rejectProcess(headers)
            assert ("处理成功" in res['msg']), f"{res}"
            logger.info("[测试通过]审批驳回合同")
        except Exception as e:
            logger.error(f"[测试失败]审批驳回合同:{e}")
            raise e
