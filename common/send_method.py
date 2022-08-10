"""
send_method.py 文件说明：
1，封装接口请求方式
    根据项目接口文档提供的内容进行封装
    不同的项目，sendmethod也不太一样，如请求体格式等。
2.封装思路-结合接口三要素
    请求方式+请求地址
    请求参数
    返回值
"""
# 导入所需模块
import jsonpath
import requests
import json
import urllib


# 封装请求模块
class SendMethod:
    """
        请求方式包括如下:
            get ---> parmas标准请求参数
            post--->请求参数类型 json
            put --->请求参数类型 json
            delete ---> parmas标准请求参数
    """

    # 定义该方法为静态方法
    @staticmethod
    def send_method(method, url, parmas=None, json=None, headers=None):
        """
        封装接口请求
        :param method: 请求方式
        :param url: 请求地址
        :param parmas: get和delete请求参数
        :param json: post和put请求参数
        :param headers: 请求头
        :return:
        """
        # 定义发送请求的方法
        if method == "get" or method == "delete":
            response = requests.request(method=method, url=url, params=parmas, headers=headers)
        elif method == "post" or method == "put":
            response = requests.request(method=method, url=url, json=json, headers=headers)
            # 如果有不同的请求头，还可以继续添加接收的参数
            # response = requests.request(method=method, url=url, json=json, data=data, files=data)
        else:
            # 这里是简单处理，完成封装需要加上异常处理。
            response = None
            print("请求方式不正确")

        # 如果请求方式是delete，只返回状态码
        # 这是根据项目接口文档中delete方法的返回规则定的。
        if method == "delete":
            return response.status_code
        else:
            # 项目中接口的返回值是json格式的，就可以用json()进行格式化返回结果。
            return response.json()

    @staticmethod
    def json_2_python(res):
        """
        格式化返回数据
        :param res:接口返回的数据
        :return:
        """
        return json.dumps(res, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    method = "get"
    url = "http://192.168.2.24:10086/prod-api/Opportunity/pageOpportunityList?current=1&size=20&opportunityName=675&customerName=%E5%90%B4&companyName=%E4%B8%8A%E6%B5%B7&createdTimeStart=2022-05-01&createdTimeEnd=2022-05-31"
    headers = {"Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTk5NTYyMzQsInVzZXJfbmFtZSI6InhpZXRhbyIsImp0aSI6ImdWWEdmSHNhMDZ1VDdUNEJxeHBGMUxXXzQyTSIsImNsaWVudF9pZCI6InRlc3RfY2xpZW50Iiwic2NvcGUiOlsicmVhZCJdfQ.j8Z2hN2kcPgtwt9CteKnqRYuEPCF6h-hwEVa0CvbDjw"}
    data = "current=1&size=20&opportunityName=675&customerName=%E5%90%B4&companyName=%E4%B8%8A%E6%B5%B7&createdTimeStart=2022-05-01&createdTimeEnd=2022-05-31"
    res = SendMethod.send_method(method=method, url=url, headers=headers)

