# -*- coding:utf-8 -*-
"""
@Created Time：2016/12/11

@author：HAO
"""
import re
import time
import unittest
from jsonpath_rw import parse
from AutoInterfaceTest.config.conf import RESPONSES, COOKIES


class CaseLayer(unittest.TestCase):
    def get_test(self, test_case):
        start_time = time.time()
        response = test_case.parameter_relevance(RESPONSES)
        RESPONSES[test_case.case_num] = response

        duration = time.time() - start_time
        print("cookies:", COOKIES)

        try:
            status_code = response.status_code
        except AttributeError:
            status_code = None

        try:
            result = response.text
        except AttributeError:
            result = None

        report_detail = """
        耗时：%(duration).3f
        响应状态：%(status)s
        请求URL：%(url)s
        请求参数: %(data)s
        请求结果：%(result)s
        """ % dict(duration=duration, status=status_code, url=test_case.url, data=test_case.req_data, result=result)
        print(report_detail)
        print(COOKIES)
        self.__assert(test_case, response)

    @staticmethod
    def getTestFunc(test_case):
        """
        装饰器方法：用来加载测试用例到此类中；
        :param test_case:
        :return:
        """

        def func(self):
            self.get_test(test_case)

        func.__doc__ = test_case.case_name
        return func

    def __assert(self, case, response):
        point = case.check_point
        try:
            data = response.json()
        except Exception:
            data = response.text

        result = "\n【请求响应结果】:\n %s" % response.text

        if isinstance(data, dict):
            try:
                for k, expected in point.items():
                    json_path_expr = parse(k)
                    actual = [str(match.value) for match in json_path_expr.find(data)]
                    actual = actual[0]
                    self.assertEqual(str(actual), expected, result)
            except AttributeError:
                self.assertEqual(data['code'], 200, result)
        elif isinstance(data, str):
            try:
                for k in point.keys():
                    expected = re.search(k, data).group(1)
                    self.assertEqual(expected, point[k])
            except AttributeError:
                self.assertLess(response.status_code, 400)
        else:
            self.assertLess(response.status_code, 400)
