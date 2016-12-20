# -*- coding:utf-8 -*-
"""
@Created Time：2016/9/6

@author：HAO
"""
import hashlib
from requests.api import get, post
from AutoInterfaceTest.config.conf import SESSION


def sort_key_and_lower_value(dict_data):
    """
    此方法：实现对请求参数（字典）key进行排序，value转化为小写，拼接返回参数字符串

    :param dict_data: Dictionary,接口请求参数
    :return: String
    """
    keys = [i for i in dict_data.keys()]
    keys.sort()
    temp = ""
    for k in keys:
        temp = "%s%s=%s&" % (temp, k, str(dict_data[k]).lower())
    return temp[0:-1]


def encrypt_of_md5(dict_data, sign):
    """
    此方法：实现对参数加盐并MD5两次生成签名
    :param dict_data: Dictionary
    :param sign: (optional)String,盐
    :return:
    """
    temp_str = sort_key_and_lower_value(dict_data) + sign
    encrypt1 = hashlib.md5(temp_str.encode()).hexdigest()
    encrypt2 = hashlib.md5(encrypt1.encode()).hexdigest()
    return encrypt2


def encryption(func):
    """
    装饰器：
    :param func:
    :return:
    """

    def wrapper(url, data, **kwargs):
        sign_value = encrypt_of_md5(data, kwargs.pop('sign', ""))
        data['sign'] = sign_value
        return func(url, data, **kwargs)

    return wrapper


@encryption
def gets(url, data=None, verify=False, **kwargs):
    return SESSION.get(url, params=data, verify=verify, **kwargs)


@encryption
def posts(url, data=None, json=None, verify=False, **kwargs):
    return SESSION.post(url, data=data, json=json, verify=verify, **kwargs)
