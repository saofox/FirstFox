# -*- coding:utf-8 -*-
"""
@Created Time：2016/12/6

@author：HAO
"""

import json
import re
from jsonpath_rw import jsonpath, parse
from AutoInterfaceTest.common.common import gets, posts
from AutoInterfaceTest.common.singletestcase import SingleTestCase
from AutoInterfaceTest.main import create_case_to_iterator


data = {'v': '3.0.2', 'jiguangToken': '1a0018970aaf340a70d', 'deviceType': '0', 'userFrom': 'baidu'}
data = str(data)
print(data)
reg_expr = '[\'\"](\S+)[\'\"]\s*:\s*[\'\"]\$(\S+)_(\S+)[\'\"]'
result_list = re.findall(reg_expr, data)

print(result_list)



# def restore_int_float(v):
#     try:
#         return int(v)
#     except ValueError:
#         try:
#             return float(v)
#         except ValueError:
#             return v
# print(restore_int_float("0.1231"))

# b = json.loads('{"code":0,"msg":"","data":{"data":[{"name":"有机","id":1,"isuploaddoc":1}, \
# {"name":"绿色","id":2,"isuploaddoc":1}, {"name":"无公害","id":3,"isuploaddoc":1}, \
# {"name":"土地认证证明","id":4,"isuploaddoc":1}]},"timestamp":1481770784889}')
#
#
# json_repx = parse('data.data[*].name')
# a = str([str(i.value) for i in json_repx.find(b)])
# print(type(a))



# file = r"E:\SheYuan-Interface\AutoInterfaceTest\testcase\TestCases.xlsx"
# for i in create_case_to_iterator(file):
#     # try:
#         # print(i.req_data)
#     result_list = re.findall('[\'\"](\S+)[\'\"]\s*:\s*[\'\"]\$(\S+)_(\S+)[\'\"]', str(i.req_data))
#     print(result_list)
#     for k, n, u in result_list:
#         print(b[n])
#         jsonpath_expr = parse(u)
#         m = [match.value for match in jsonpath_expr.find(b[n])]
#         print(m[0])
#         # try:

# except KeyError:
#     print("key1")
# except KeyError:
#     print("key")
# except AttributeError:
#     print("search")


# expected = "{friends:[{id:123,name:\"Corby Page\"},{id:456,name:\"Carter Page\"}]}";
# JSONAssert.assertEquals(expected, data, false);


# a = '$.code=0'
# b = SingleTestCase.check_point_parser(a)
# print(b)
# input_args1 = {'userToken': 'abb5feaa322644b8a77775cf8f40e8f3', 'v': '3.0.2', 'type': '1'}
#
# response1 = gets("https://123.sheyuan.com/v3/goods/getlist", data=input_args1, sign="sheyuanhui")
# res = response1.json()
# for x, y in b.items():
#     print(x)
#     jsonpath_expr = parse(x)
#     for i in [match.value for match in jsonpath_expr.find(res)]:
#         print(y == i)







# # data1 = '{"code":0,"msg":"","data":{"result":[{"prodtUuid":"c8cfddda-3a40-4c4a-b71c-7a240cf1a9a2","mainImage":"http://syimg.sheyuan.com/2016/11/02/1cfa5160-792b-4bc6-a2b3-109b006990dd.jpg","checkStatus":1,"statusUn":1,"serialNumber":"71903","statusDesc":null,"goodsStatus":0,"goodsPrice":0.01,"id":2811,"selledNum":1622,"inventory":1000,"goodsName":"冠军梨［山西特别］今日特价0.01一斤"}],"typenum":[{"num":1,"tp":1}, {"num":0,"tp":2}],"type":1},"timestamp":1481032477829}'
# # regular_result = re.search('prodtUuid":"(\S+?)"', data1).group(1)
# # print(regular_result)
#
# input_args2 = '{"userToken": "a8fe53c9c31944f18ada751e1c5a14cf", "v": "3.0.2", "action": "1","prodtUuid":"$prodtUuid"}'
# data2 = json.loads(input_args2, encoding="utf-8")
# print("data2:", data2)
#
# regular_list = re.findall('\$(\w+)', input_args2)
#
# for i in regular_list:
#     regular_search = '%s":"(\S+?)"' % i
#     data2[i] = re.search(regular_search, data1).group(1)
#
# response2 = gets("https://123.sheyuan.com/v3/goods/editGoodsStatus", data=data2, sign="sheyuanhui")
#
# print(json.loads(response2.content.decode("utf-8")))

# s = re.findall('[\'\"](\S+)[\'\"]\s*:\s*[\'\"]\$(\S+)_(\S+)[\'\"]',
#                "{'sign'     :    '$test01_123', 'v': '$test02_asdsa', 'jiguangToken': '140fe1da9ea2e7ff14e', 'deviceType': '0', 'password': '95AC390DCB2F090267F8E635440917E7', 'mobile': '18600231840'}")
# print(s)

# param = "jiguangToken=140fe1da9ea2e7ff14e&deviceType=0&mobile=18600231840&password=95AC390DCB2F090267F8E635440917E7&sign=A5B36134EAA2B40B6470B983816A8F4E&v=3.0.2"
#
# print(str(dict([p.split("=") for p in param.split("&")])))


# class ObjectTest:
#     def __init__(self, d):
#         self.__dict__ = d
#
#
# s = '{"code":0,"msg":"","data":{"bgImgUrl":"http://syimg.sheyuan.com/upload/staticResource/2016/10581173e2ebe2323719c6878d/177ab55f-f0f9-4a73-b038-eabd025c33be.jpg","linkUrl":"https://www.baidu.com/","appSignKey":"sheyuanhui","appVersionInfo":null,"imgVisitUrl":"http://syimg.sheyuan.com"},"timestamp":1481269175421}'
#
#
# def abc(string):
#     return string.replace("'",'"')
#
# print(abc(s))


# s = r"""C:\Python35\lib\site-packages\requests\packages\urllib3\connectionpool.py:821: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.org/en/latest/security.html
#   InsecureRequestWarning)
# 时长：0.348085880279541
#         请求URL：https://123.sheyuan.com/v3/farm/systemConfig
#         请求参数: {'v': '3.0.2', 'deviceType': '0', 'sign': '8757021166d25eea4b9bc50cba617ebb'}
#         请求结果：{"code":0,"msg":"","data":{"bgImgUrl":"http://syimg.sheyuan.com/upload/staticResource/2016/10581173e2ebe2323719c6878d/177ab55f-f0f9-4a73-b038-eabd025c33be.jpg","linkUrl":"https://www.baidu.com/","appSignKey":"sheyuanhui","appVersionInfo":null,"imgVisitUrl":"http://syimg.sheyuan.com"},"timestamp":1481698609312}"""
#
# import os
# print(str(["asd","adsad"]))
