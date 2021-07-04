# -*- coding: utf-8 -*-
# @Time    : 2021/7/4 4:31 下午
# @File    : sds_string.py
# @Software: PyCharm

# 简单动态字符串

class SdsString(object):
    def __init__(self):
        self.len = 0  # 长度
        self.free = 0  # 未使用的长度
        self.buf = list()  # 用于保存字符串
        self.sds_str = ''

    def app_space(self, str_info):
        """
        申请空间
        :return:
        """

        self.free = self.len * 2 + 1 - self.len - 1

    def append(self, str_info: str):
        """

        :param str_info:
        :return:
        """
        if self.len > 0:
            self.buf = self.buf[:-1]
        self.len += len(str_info)

        # app space
        self.app_space(str_info)

        for s in str_info:
            self.buf.append(s)
        self.buf.append(' ')

    def __str__(self):
        return ''.join(self.buf)

    def print_info(self):
        print("app space free", self.free)
        print("len", self.len)
        print("buf", self.buf)
        print("str", self)
        print("="*20)


if __name__ == '__main__':
    sds = SdsString()
    sds.append("abc")
    sds.print_info()
    sds.append("123")
    sds.print_info()
    sds.append(" ")
    sds.print_info()



