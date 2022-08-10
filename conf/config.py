import os

"""(1)接口地址"""
testIP = "http://192.168.2.24:10086/prod-api"
TIME_OUT = 30
user = {"username":"jiangyan","password":"a123456","verificationCode":"悠悠"}

"""(2)测试文件路径"""
# 框架项目顶层目录的绝对路径
project_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
# 测试报告路径
testcase_dir = os.path.join(project_dir,"testCase")
# 测试数据路径
testdata_dir = os.path.join(project_dir,"data")

"""(3)数据库连接配置"""
oca = {"host": "192.168.2.120", "user": "root", "password": "123456", "database": "erp_oca", "charset": "utf8"}
crm = {"host": "192.168.2.120", "user": "root", "password": "123456", "database": "erp_crm", "charset": "utf8"}
msm = {"host": "192.168.2.120", "user": "root", "password": "123456", "database": "erp_msm", "charset": "utf8"}
