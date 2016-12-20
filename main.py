# -*- coding:utf-8 -*-
"""
@Created Time：2016/12/8

@author：HAO
"""
import logging
import unittest
import HTMLTestRunner
from AutoInterfaceTest.common.caselayer import CaseLayer
from AutoInterfaceTest.common import excelparser
from AutoInterfaceTest.common.singletestcase import SingleTestCase


def create_case_to_iterator(excel):
    cases = excelparser.get_test_case(excel)
    for ca in cases:
        yield SingleTestCase(ca)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s  %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S'
                        )

    logging.info("开始执行测试用例！")

    # 读取excel中每条记录，将每条记录实例化为SingleTestCase对象，并加入CaseLayer中，真正形成一条测试用例；
    file = r"E:\SheYuan-Interface\AutoInterfaceTest\testcase\TestCases.xlsx"
    for i in create_case_to_iterator(file):
        setattr(CaseLayer, "%s" % i.case_num, CaseLayer.getTestFunc(i))

    case_layer = CaseLayer()
    test_suite = unittest.TestSuite()
    for c in dir(case_layer):
        if c.startswith("TEST"):
            test_suite.addTest(CaseLayer(c))
    if test_suite.countTestCases() is None:
        raise Exception("ERROR：测试用例没有加载成功！")

    filePath = r"E:\SheYuan-Interface\AutoInterfaceTest\report\report.html"
    with open(filePath, "wb") as html_report:
        runner = HTMLTestRunner.HTMLTestRunner(html_report)
        result = runner.run(test_suite)
    logging.info("*****ALL TestCase Perform Finish!!*****")
