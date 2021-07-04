# -*- coding: utf-8 -*-
# @Time    : 2021/7/4 4:37 下午
# @File    : dict_hc.py
# @Software: PyCharm

# 字典
# 哈希表

# 字典
class DictObj(object):
    def __init__(self):
        self.dict_hcs = list()  # 包含两个哈希表，一个用于保存数据，一个在rehash时使用
        self.rehash_idx = None  # rehash记录位置时使用


# 哈希表
class DictHc(object):
    def __init__(self):
        self.dict_entry_list = list()  # 哈希表节点
        self.len = 0  # 哈希表长度
        self.max_index = None  # 最大索引值 = len - 1


# 哈希节点
class DictEntry(object):
    def __init__(self, key, value):
        self.value = value  # 值
        self.key = key  # key
        self.next = None  # 指向下一个节点的指针

