# -*- coding:utf-8 -*-
"""
@Created Time：2016/12/7

@author：HAO
"""

import xlrd


def open_excel(excel_file, sheet_index=0):
    try:
        test_case = xlrd.open_workbook(excel_file)

        return test_case.sheet_by_index(sheet_index)
    except Exception as e:
        print(e)


def get_test_case(excel_file):
    table = open_excel(excel_file)
    temp_record = []
    multiple_record = []

    for row in range(1, table.nrows):
        for col in range(0, table.ncols):
            value = table.cell_value(row, col)
            temp_record.append(value)

        multiple_record.append(temp_record)
        temp_record = []

    return multiple_record


# print(get_test_case(r"E:\SheYuan-Interface\AutoInterfaceTest\testcase\TestCases.xlsx"))




