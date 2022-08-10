import logging
import time
import unittest
import HTMLTestRunner
import os
from conf import config
from common import mylog

# # 定位测试用例目录(可以再封装)
# project_dir = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) )
# #testcase_dir = project_dir + r"\testCase"
# testcase_dir = os.path.join(project_dir,"testCase")

def creatsuite():
    '''获取测试集'''
    # 搜索测试用例
    testcases = unittest.defaultTestLoader.discover(config.testcase_dir, pattern="test*.py", top_level_dir=None)
    return testcases

def run(title=u'自动化测试报告', description=u'众灿互动ERP系统'):
    """执行测试并生成报告"""

    # 如果没有测试报告目录自动创建
    for filename in os.listdir(config.project_dir):
        if filename == "report":
            break
    else:
        os.mkdir(config.project_dir + r'\report')

    # 执行测试用例并生成测试报告
    # 1 确定测试报告存放路径
    report_path = config.project_dir + r'\report'
    print(report_path)
    # 2 确定测试报告名称
    now = time.strftime("%Y_%m_%d_%H-%M-%S")
    report_file = report_path + "\\" + now + "report.html"  # 测试报告文件名

    # 打开文件并写入
    with open(report_file, "wb") as fp:
        # 实例化
        """
            title：报告的标题
            description：报告的描述
            stream:执行结果全部卸载该文件纵
            verbosity：报告的详细程度，0.1.2 ，2为最详细
            retry：重试，这个是坏的，不能用
        """
        runner = HTMLTestRunner.HTMLTestRunner(
            title=title,
            description=description,
            verbosity=2,
            stream=fp
        )
        runner.run(creatsuite())

if __name__ == '__main__':
    mylog.configLog()
    logger = logging.getLogger('logger')
    logger.info('-begin test！')
    run()
    logger.info('-end test！')