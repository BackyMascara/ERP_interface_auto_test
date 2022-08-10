"""
getKeyword_forResult.py文件说明：
1.作用
    在接口返回值中，通过关键获取获取对应字段内容
2.前提：需要安装一个库：jsonpath库
    安装jsonpath ： pip install jsonpath
    使用jsonpath模块进行处理更加方便
3.嵌套n层也能取到所有keyword信息，
  其中："$"表示最外层的{}，
  ".."表示模糊匹配
"""
# 导入jsonpath模块
import jsonpath


# 封装获取接口返回值方法
class GetKeyword:
    # 定义成一个静态方法
    @staticmethod
    def get_keyword(response: dict, keyword):
        """
        通过关键字获取对应返回值,如果有多个值,只返回第一个,
        如果关键字不存在,返回False。
        :param:response 数据源  字典格式
        :param:keyword 要获取的字段
        :return:
        """
        try:
            return jsonpath.jsonpath(response, f"$..{keyword}")[0]
        except:
            print("关键字不存在")

    @staticmethod
    def get_keywords(response: dict, keyword):
        """
        通过关键字获取一组数据
        :param response: 数据源 dict格式
        :param keyword:  如果关键字不存在,返回False
        :return:
        """
        try:
            return jsonpath.jsonpath(response, f"$..{keyword}")
        except:
            print("关键字不存在")


if __name__ == '__main__':
    response = {
        "count": 2,
        "next": "下一页",
        "previous": None,
        "results": [
            {
                "dep_id": "10",
                "dep_name": "tester_10",
                "master_name": "master_10",
                "slogan": "随便"
            },
            {
                "dep_id": "11",
                "dep_name": "tester_11",
                "master_name": "master_11",
                "slogan": "随便"
            }
        ]
    }
    keyword = "master_name"
    # print(GetKeyword.get_keyword(response, keyword))
    print(GetKeyword.get_keywords(response, keyword))

