import unittest
import urllib.parse

from interface.base.login import Login
from conf import config
from interface.crm.brand import Brand
import logging

logger = logging.getLogger("logger")

class Test_Get_Brand(unittest.TestCase):
    """
    参数有：brandName、platform、userName、current、size
    """
    @classmethod
    def setUpClass(cls) -> None:
        cls.login = Login()
        cls.access_token = cls.login.get_access_token("xietao")
        cls.headers = {"Authorization": cls.access_token}
        try:
            cls.url = "{}/crm/Brand/getByBrandName".format(config.testIP)
            cls.brand = Brand(cls.url)
            logger.info("=======【品牌管理】投放账号列表测试开始=======")
        except Exception as e:
            logger.error(f'实例化Brand失败:{e}')
            raise e

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("=======【品牌管理】投放账号列表测试结束=======")

    def test_get_brand_01(self):
        """根据投放账号查询品牌"""
        userName = "小"
        # get请求传中文值，需要转义
        data = f"brandName=%E5%94%B1%E5%90%A7&platform=1&userName={urllib.parse.quote(userName)}&current=1&size=20"
        try:
            res = self.brand.getByBrandName(data,self.headers)
            if len(res["data"]["records"]) != 0:
                userNames = self.brand.get_keywords(res,"userName")
                for u in userNames:
                    assert (userName in u),"投放账号不一致"
            else:
                print("没有查询结果！")
            logger.info("[测试通过]根据投放账号查询品牌，结果正确")
        except Exception as e:
            logger.error(f"[测试失败]根据投放账号查询品牌，结果正确:{e}")
            raise e

    def test_get_brand_02(self):
        """根据品牌名称查询品牌"""
        brandName = "唱吧"
        # get请求传中文值，需要转义
        data = f"brandName={urllib.parse.quote(brandName)}&platform=1&current=1&size=20"
        try:
            res = self.brand.getByBrandName(data,self.headers)
            if len(res["data"]["records"]) != 0:
                brandNames = self.brand.get_keywords(res,"brandName")
                for b in brandNames:
                    assert (brandName in b),"品牌名称不一致"
            else:
                print("没有查询结果！")
            logger.info("[测试通过]根据品牌名称查询品牌，结果正确")
        except Exception as e:
            logger.error(f"[测试失败]根据品牌名称查询品牌，结果正确:{e}")
            raise e

    def test_get_brand_03(self):
        """根据板块查询品牌"""
        platform = 3
        data = f"brandName=%E7%BE%8E%E5%A6%86%5B%E8%B6%85%E8%AF%9D%5D&platform={platform}&current=1&size=20"
        try:
            res = self.brand.getByBrandName(data,self.headers)
            if len(res["data"]["records"]) != 0:
                platforms = self.brand.get_keywords(res,"platform")
                for p in platforms:
                    assert (platform == p),"板块不一致"
            else:
                print("没有查询结果！")
            logger.info("[测试通过]根据板块查询品牌，结果正确")
        except Exception as e:
            logger.error(f"[测试失败]根据板块查询品牌，结果正确:{e}")
            raise e

    def test_get_brand_04(self):
        """测试投放账号窗口的分页功能"""
        current = 4
        size = 50
        data = f"current={current}&size={size}&brandName=%E5%94%B1%E5%90%A7&platform=1"
        try:
            res = self.brand.getByBrandName(data,self.headers)
            if len(res["data"]["records"]) != 0:
                assert (current == res["data"]["current"]),"当前页不一致"
                assert (size == res["data"]["size"]),"分页数不一致"
            else:
                print("没有查询结果！")
            logger.info("[测试通过]测试投放账号窗口的分页功能，结果正确")
        except Exception as e:
            logger.error(f"[测试失败]测试投放账号窗口的分页功能，结果正确:{e}")
            raise e


if __name__ == '__main__':
    unittest.main()