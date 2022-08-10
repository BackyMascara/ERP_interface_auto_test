import json
import logging
import unittest
from interface.crm.brand import Brand
from interface.organization.login import Login
from conf import config

logger = logging.getLogger('logger')

class Test_Brand_List(unittest.TestCase):
    """
    参数有：brandName、platform、timesStart、timesEnd、current、size
    """
    @classmethod
    def setUpClass(cls) -> None:
        # 获取鉴权
        cls.login = Login()
        cls.access_token = cls.login.get_access_token("xietao")
        cls.headers = {"Authorization": cls.access_token}
        try:
            # 实例化Brand类
            cls.url = '{}/crm/Brand/pageBrandForViewList'.format(config.testIP)
            cls.brand = Brand(cls.url)
            logger.info('=======【品牌管理】品牌列表测试开始=======')
        except Exception as e:
            logger.error(f'实例化Brand失败:{e}')
            raise e

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info('=======【品牌管理】品牌列表测试结束=======')

    def test_search_brand_01(self):
        '''根据品牌名称查询(size默认10)'''
        data = {
            "brandName":'哈哈'
        }
        try:
            res = self.brand.pageBrandForViewList(data,self.headers) # 查询结果
            brands = self.brand.get_keywords(res,"brandName") # 获取结果中的brandName
            if len(res["data"]["records"]) != 0:
                for b in brands:
                    # 这里有第一个坑：查询结果不分大小写，但是Python是区分大小写的
                    assert (data["brandName"].lower() in str(b).lower()),"品牌名称不一致"
            else:
                print("没有查询结果")
            logger.info('[测试通过]根据品牌名称查询，结果正确')
        except Exception as e:
            logger.error(f'[测试失败]根据品牌名称查询，结果正确:{e}')
            raise e

    def test_search_brand_02(self):
        '''根据投放平台查询(size默认10)'''
        data = {
            "platform":'1'
        }
        try:
            res = self.brand.pageBrandForViewList(data, self.headers)
            platforms = self.brand.get_keywords(res,"platform")
            if len(res["data"]["records"]) != 0:
                for p in platforms:
                    # 这里有第二个坑：data["platform"]是string，p是int
                    assert (data["platform"] in str(p)),"投放平台不一致"
            else:
                print("没有查询结果")
            logger.info('[测试通过]根据投放平台查询，结果正确')
        except Exception as e:
            logger.error(f'[测试失败]根据投放平台查询，结果正确:{e}')
            raise e

    def test_search_brand_03(self):
        """按投放次数查询(size默认10)"""
        data = {
            "timesStart":20,
            "timesEnd":100
        }
        try:
            res = self.brand.pageBrandForViewList(data,self.headers)
            times = self.brand.get_keywords(res,"times")
            if len(res["data"]["records"]) != 0:
                for t in times:
                    # 这里有第三个坑：range(x,y)是不包含y的
                    assert (t in range(data["timesStart"],data["timesEnd"]+1)),"投放次数不在区间内"
            else:
                print("没有查询结果")
            logger.info("[测试通过]按投放次数查询，结果正确")
        except Exception as e:
            logger.error(f"[测试失败]按投放次数查询，结果正确:{e}")
            raise e

    def test_search_brand_04(self):
        """测试品牌管理的分页功能"""
        data = {
            "current":3,
            "size":50
        }
        try:
            res = self.brand.pageBrandForViewList(data,self.headers)
            if len(res["data"]) != 0:
                assert (data["current"] == res["data"]["current"]),"当前页不一致"
                assert (data["size"] == res["data"]["size"]),"分页数不一致"
            else:
                print("没有查询结果！")
            logger.info("[测试通过]测试品牌管理的分页功能，结果正确")
        except Exception as e:
            logger.error(f"[测试失败]测试品牌管理的分页功能，结果正确:{e}")
            raise e

    def test_search_brand_05(self):
        '''组合查询品牌'''
        data = {
            "brandName": "R",
            "platform": "1",
            "timesStart": 100,
            "timesEnd": 200,
            "current": 1,
            "size": 20
        }
        try:
            res = self.brand.pageBrandForViewList(data, self.headers)  # 查询结果
            brands = self.brand.get_keywords(res, "brandName")  # 获取结果中的brandName
            platforms = self.brand.get_keywords(res,"platform")
            times = self.brand.get_keywords(res,"times")
            print(res)
            if len(res["data"]["records"]) != 0:
                assert (data["current"] == res["data"]["current"]),"当前页不一致"
                assert (data["size"] == res["data"]["size"]), "分页数不一致"
                for b in brands:
                    assert (data["brandName"].lower() in str(b).lower()),"品牌名称不一致"
                for p in platforms:
                    assert (data["platform"] in str(p)),"投放平台不一致"
                for t in times:
                    assert (t in range(data["timesStart"],data["timesEnd"]+1)),"投放次数不一致"
            else:
                print("没有查询结果")
            logger.info("[测试通过]组合查询品牌，结果正确")
        except Exception as e:
            logger.error(f"[测试失败]组合查询品牌，结果正确:{e}")
            raise e


if __name__ == '__main__':
    unittest.main()