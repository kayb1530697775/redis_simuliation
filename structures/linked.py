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

    def __str__(self):
        return self.value


class LinkedList(object):
    def __init__(self):
        self.head_node = None  # 头部节点
        self.end_node = None  # 尾部节点
        self.len = 0  # 链表长度

    def insert(self, pos, value):
        """
        插入一个值
        :param pos:
        :param value:
        :return:
        """

        if pos < 0:
            raise Exception("pos params must > 0")

        if pos >= self.len:
            self.append(value)
        else:
            l_node = LinkedNode(value)

            now_pos_node = self.head_node
            i = 0
            while i != pos:
                now_pos_node = now_pos_node.next
                i += 1

            # 新节点的前一个节点 = 当前位置节点的前一个节点
            l_node.pre = now_pos_node.pre
            # 新节点的下个节点 = 当前位置的节点
            l_node.next = now_pos_node

            # 将新的节点放入链表中
            if pos == 0:  # 如果是0的位置 则修改头部
                self.head_node = l_node
            else:  # 如果不是0的位置 需要将 当前前一个的节点的下一个节点修改为新的节点
                now_pos_node.pre.next = l_node

            # 当前节点的前一个节点修改为新节点
            now_pos_node.pre = l_node

            self.len += 1


    def append(self, value):
        """
        添加一个元素
        :param value:
        :return:
        """
        l_node = LinkedNode(value)

        if self.len == 0:
            self.head_node = l_node
            self.end_node = l_node
        else:
            # 当前最后一个节点的下一个节点 指向 新节点
            self.end_node.next = l_node

            # 新节点的前一个节点指向当前的最后一个节点

            l_node.pre = self.end_node

            # 修改尾部节点
            self.end_node = l_node

        self.len += 1

    def print_info(self, backward):
        """
        打印双端列表
        :return:
        """
        print("head", self.head_node)
        print("end", self.end_node)
        print("len", self.len)

        if backward:
            self.print_info_next()
        else:
            self.print_info_pre()

    def print_info_next(self):
        """
        向后打印
        :return:
        """
        l_node = self.head_node

        while l_node:
            print(l_node)
            l_node = l_node.next

    def print_info_pre(self):
        """
        向前打印
        :return:
        """
        l_node = self.end_node

        while l_node:
            print(l_node)
            l_node = l_node.pre


if __name__ == '__main__':

    ll = LinkedList()
    ll.append("abc")
    ll.append("efg")
    ll.append("hij")
    ll.append("klm")
    ll.append("nop")
    ll.insert(1, "d")
    ll.insert(2, "c")
    ll.insert(3, "b")
    ll.insert(4, "a")
    ll.print_info(0)

