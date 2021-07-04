# -*- coding: utf-8 -*-
# @Time    : 2021/7/4 4:34 下午
# @File    : linked.py
# @Software: PyCharm

# 链表

class LinkedNode(object):
    def __init__(self, value):
        self.pre = None  # 前置节点
        self.next = None  # 后置节点
        self.value = value  # 节点值


class LinkedList(object):
    def __init__(self):
        self.head_node = None  # 头部节点
        self.end_node = None  # 尾部节点
        self.len = 0  # 链表长度



