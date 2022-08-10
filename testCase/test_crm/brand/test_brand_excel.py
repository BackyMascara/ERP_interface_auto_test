import logging
import unittest
from interface.base.login import Login
from interface.crm.brand import Brand
from conf import config

from common.opreation_excel import OperationExcel
import ddt

logger = logging.getLogger("logger")
# 获得数据文件
oper = OperationExcel(config.testdata_dir+'\search_brand.xls')
# 获取数据
test_data = oper.get_data_by_dict()

@ddt.ddt()
class Test_Brand_Excel(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # 实例化Login类
        cls.login = Login()
        cls.access_token = cls.login.get_access_token("xietao")
        cls.headers = {"Authorization": cls.access_token}
        try:
            # 实例化Brand类
            cls.url = '{}/crm/Brand/pageBrandForViewList'.format(config.testIP)
            cls.brand = Brand(cls.url)
            logger.info('=======【品牌管理】数据驱动测试开始=======')
        except Exception as e:
            logger.error(f'实例化Brand失败:{e}')
            raise e

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info('=======【品牌管理】数据驱动测试结束=======')

    @ddt.data(*test_data)
    def test_search_brand(self, data): # 5.出入data参数
        '''查询品牌'''
        req_data = {
            "brandName": data['brandName'],
            "platform": data['platform'],
            "timesStart": data['timesStart'],
            "timesEnd": data['timesEnd']
        }
        try:
            res = self.brand.pageBrandForViewList(req_data,self.headers)
            print(res)
            assert (res['msg'] in data['expect']),"与预期结果不对应"
        except Exception as e:
            logger.error(f"[测试失败]查询品牌，结果正确:{e}")
            raise e

if __name__ == '__main__':
    unittest.main()