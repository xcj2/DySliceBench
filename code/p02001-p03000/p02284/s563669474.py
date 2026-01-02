# -*- coding: utf-8 -*-

import random
import sys
import os


class Tree:
    def __init__(self):
        self.root = None

    def __str__(self):
        if self.root == None:
            return None
        else:
            return "TODO"

    def print_inorder(self):
        self.inorder_list = []
        self.__inorder(self.root)
        return self.inorder_list

    def __inorder(self, node):
        """
        :param node: Node
        :return:
        """
        if node is None:
            return
        else:
            self.__inorder(node.left)
            self.inorder_list.append(node.key)
            self.__inorder(node.right)

    def print_preorder(self):
        self.preorder_list = []
        self.__preorder(self.root)
        return self.preorder_list

    def __preorder(self, node):
        """
        :param node: Node
        :return:
        """
        if node is None:
            return
        else:
            self.preorder_list.append(node.key)
            self.__preorder(node.left)
            self.__preorder(node.right)

    def insert(self, node):
        """
        :param node: Node
        :return:
        """
        if self.root is None:
            self.root = node
        else:
            x = self.root
            parent_candidate = x

            while x is not None:
                parent_candidate = x
                if x.key > node.key:
                    x = x.left
                else:
                    x = x.right

            # child to parent link
            x = node
            x.parent = parent_candidate

            # parent to child link
            if x.key < x.parent.key:
                x.parent.left = x
            else:
                x.parent.right = x

    def find(self, value):
        """
        :param value:
        :rtype: Node
        :return:
        """
        x = self.root
        while x is not None and x.key != value:
            if x.key > value:
                x = x.left
            else:
                x = x.right
        return x

    def delete(self, value):
        found_node = self.find(value)
        if found_node is None:
            print("value is nothing")
        else:
            # has no child
            if found_node.is_leaf():
                # delete link from parent
                print(found_node.parent.left.key)
                print(found_node.key)

                if found_node.parent.left.key == found_node.key:
                    found_node.parent.left = None
                else:
                    found_node.parent.right = None
            else:
                # has one child
                if found_node.has_one_child():
                    one_child = found_node.get_one_child()

                    # change link to parent
                    one_child.parent = found_node.parent

                    # chagne link from parent
                    if found_node.parent.left == found_node:
                        found_node.parent.left = one_child
                    else:
                        found_node.parent.right = one_child

                # has two child
                else:
                    next_section_point = found_node.get_next_section_point()
                    # ?¬???????????????????????????????????????????????¬?????????????????????? p217
                    # ????????????
                    key = next_section_point.key
                    self.delete(next_section_point.key)
                    found_node.key = key


class Node:
    def __init__(self, key):
        self.parent = None  # type: Node
        self.left = None  # type: Node
        self.right = None  # type: Node
        self.key = key  # type: int

    def has_one_child(self):
        if self.left is None and self.right is not None:
            return True
        elif self.left is not None and self.right is None:
            return True
        else:
            return False

    def get_one_child(self):
        if not self.has_one_child():
            return None
        else:
            if self.left is not None:
                return self.left
            else:
                return self.right

    def get_next_section_point(self):
        """?¬??????????????????????"""

        # ????????????????????´???
        if self.right is not None:
            return self.right.get_minimum()
        # ???????????????????????´???????¬???????????????´?????????
        else:
            # ?
            return self.parent

    def is_leaf(self):
        if self.left is None and self.right is None:
            return True
        else:
            return False

    def get_minimum(self):
        if self.left is None:
            return self
        else:
            return self.left.get_minimum()

tree = Tree()
s = input()
n = int(s)
for _ in range(n):
    s = input()
    if 'insert' in s:
        value = int(s.split(" ")[-1])
        node = Node(value)
        tree.insert(node)

    if 'print' in s:
        in_list = tree.print_inorder()
        in_list = map(str, in_list)
        print(' ' + ' '.join(in_list))

        pre_list = tree.print_preorder()
        pre_list = map(str, pre_list)
        print(' ' + ' '.join(pre_list))

    if 'find' in s:
        value = int(s.split(" ")[-1])
        node = tree.find(value)
        if node is None:
            print('no')
        else:
            print('yes')