# -*- coding:utf-8 -*-
"""
@Created Time：2016/12/8

@author：HAO
"""

import logging
import re

from jsonpath_rw import parse
from requests.cookies import cookiejar_from_dict
from AutoInterfaceTest.common.common import gets, posts
from AutoInterfaceTest.config.conf import SESSION, COOKIES, SIGN


def reg_of_param(data):
    reg = """["'](.[^:"']+?)["']\s*:\s*["']\$(.+?)_\{(.+?)\}"""
    result_list = re.findall(reg, str(data))
    return result_list


    # response = '{"code":0,"msg":"","data":{"token":"cda58b67a5334d3ab23ebd20ab385aca"},"timestamp":1481685953405}'
    # print(re.search('userToken":"(\S+?)"', response).group(1))


    # if len(result_list) != 0:
    #
    #     for k, n, u in result_list:
    #         print("参数名：", k, "用例名：", n, "关联参数名：", u)
    #
    #         """
    #             测试用例中请求参数格式："key":"$CaseNum_UpKey"
    #             参数关联：根据CaseNum从响应结果集中获取对应的响应结果列，再根据UpKey从响应结果中获取对应的参数值，并赋值给当前请求参数key；
    #
    #             :key k  Key     参数名 （本次请求中的参数名）
    #             :key n  CaseNum 用例编号（根据CaseNum从响应结果集中获取对应的响应结果）
    #             :key u  UpKey   关联参数名（此前请求响应中返回的参数名）
    #         """
    #         logging.debug("需要从【%s 】用例 响应中获取关联参数: %s 的值：%s" % (n, u, response[n].json()))
    #         try:
    #             expr = parse(u)
    #             m = [match.value for match in expr.find(response[n].json())]
    #
    #             try:
    #                 m = m[0]
    #             except IndexError:
    #                 logging.error("未从【%s】响应结果中匹配到所需的参数！" % response[n])
    #             self.req_data[k] = m
    #             SingleTestCase.__add_cookies_custom(k, m)
    #
    #             # search_regular = '%s":"(\S+?)"' % u
    #             # self.req_data[k] = re.search(search_regular, str(response[n])).group(1)
    #         except AttributeError:
    #             logging.error("【%s】请求参数[%s]未能从响应结果中匹配到参数,请检查接接口请求参数是否填写正确！！！" % (self.case_name, k))


class SingleTestCase:
    def __init__(self, case):
        self.case_num = case[0]
        self.case_name = case[1]
        self.api_host = case[2]
        self.api_url = case[3]
        self.req_method = case[4]

        self.req_data = SingleTestCase.__parser(case[5])
        self.check_point = SingleTestCase.__parser(case[6])
        self.is_sign = case[7]
        self.cookie = SingleTestCase.__parser(case[8])
        self.is_active = case[9]

        self.url = self.api_host + self.api_url

    @staticmethod
    def __parser(param):
        if len(param) != 0:
            try:
                d = dict([p.split("=", maxsplit=1) for p in param.split("&")])
                return d
            except Exception:
                pass
        return param

    # @staticmethod
    # def __restore_int_float(v):
    #     try:
    #         return int(v)
    #     except ValueError:
    #         try:
    #             return float(v)
    #         except ValueError:
    #             return v

    def test_runner(self):

        if isinstance(self.req_data, str) or isinstance(self.req_data, bytes):
            self.req_data = eval(self.req_data)

        if self.req_method.upper() == "GET" and self.is_sign.upper() == "YES":
            response = gets(self.url, self.req_data, sign=SIGN)
            return response

        elif self.req_method.upper() == "GET" and self.is_sign.upper() == "NO":
            response = SESSION.get(self.url, params=self.req_data, verify=False)
            return response

        elif self.req_method.upper() == "POST" and self.is_sign.upper() == "YES":
            response = posts(self.url, self.req_data, sign=SIGN)
            return response

        elif self.req_method.upper() == "POST" and self.is_sign.upper() == "NO":
            response = SESSION.post(self.url, self.req_data, verify=False)
            return response

    # @staticmethod
    # def __add_cookies_custom(k, m):
    #     cookiejar_from_dict({k: m}, COOKIES)

    def parameter_relevance(self, response=None):
        if response is not None:
            req_data_list = reg_of_param(self.req_data)
            cookie_list = reg_of_param(self.cookie)

            if len(req_data_list) != 0:
                # for k, n, u in req_data_list:
                #     try:
                #         expr = parse(u)
                #         m = [match.value for match in expr.find(response[n].json())]
                #         m = m[0]
                #         self.req_data[k] = m
                #     except Exception:
                #         try:
                #             reg_result = re.search(u, response[n].text).group(1)
                #             self.req_data[k] = reg_result
                #         except IndexError:
                #             pass
                for k, n, u in req_data_list:
                    try:
                        expr = parse(u)
                        m = [match.value for match in expr.find(response[n].json())][0]
                    except Exception:
                        try:
                            m = re.search(u, response[n].text).group(1)
                        except IndexError:
                            pass
                    self.req_data[k] = m

            if len(cookie_list) != 0:
                for k, n, u in cookie_list:
                    try:
                        expr = parse(u)
                        m = [match.value for match in expr.find(response[n].json())][0]
                    except Exception:
                        try:
                            m = re.search(u, response[n].text).group(1)
                        except IndexError:
                            pass
                    cookiejar_from_dict({k: m}, COOKIES)

                        # for k, n, u in cookie_list:
                        #     expr = parse(u)
                        #     m = [match.value for match in expr.find(response[n].json())]
                        #     m = m[0]
                        #     cookiejar_from_dict({k: m}, COOKIES)

                        # SingleTestCase.__add_cookies_custom(k, m)

        return self.test_runner()
