#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
input:
10
insert 30
insert 88
insert 12
insert 1
insert 20
find 12
insert 17
insert 25
find 16
print

output: finded + in_order + pre_order
yes
no
 1 12 17 20 25 30 88
 30 12 1 20 17 25 88

"""

import sys


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left, self.right = None, None

    def insert(self, data):
        """
        insert data according to BST rules
        """
        if data < self.data:
            if not self.left:
                self.left = Node(data)
            else:
                self.left.insert(data)
        # insert duplicate value to right
        else:
            if not self.right:
                self.right = Node(data)
            else:
                self.right.insert(data)

        return self.data

    def find(self, data, parent=None):
        """
        find node with given data
        tree walk as insert goes
        """
        if data < self.data:
            if not self.left:
                return None, None
            return self.left.find(data=data, parent=self)
        elif data > self.data:
            if not self.right:
                return None, None
            return self.right.find(data=data, parent=self)
        else:
            return self, parent

    def children_count(self):
        """
        for choosing node deleting strategy
        """
        cnt = 0
        if self.left:
            cnt += 1
        if self.right:
            cnt += 1
        return cnt

    def delete(self, data):
        """
        delete node with given data
        """
        node, parent = self.find(data)
        if node:
            children_count = node.children_count()
            if children_count == 0:
                # delete reference to parent
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
                del node
            elif children_count == 1:
                # node's son becomes parents' son
                if node.left:
                    n = node.left
                else:
                    n = node.right
                if parent:
                    if parent.left is node:
                        parent.left = n
                    else:
                        parent.right = n
                del node
            else:
                parent = node
                successor = node.right
                # recursively find deepest successor
                while successor.left:
                    parent = successor
                    successor = successor.left
                    
                # replace node with node.next(in-order)
                node.data = successor.data
                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right
                del node


def pre_order(node):
    if node:
        print('', node.data, end='')
        pre_order(node.left)
        pre_order(node.right)
    return None


def in_order(node):
    if node:
        in_order(node.left)
        print('', node.data, end='')
        in_order(node.right)
    return None


def action(command, content):
    # start all action from tree_root
    if command.startswith('in'):
        tree_root.insert(int(content))

    elif command.startswith('fi'):
        if tree_root.find(int(content)) == (None, None):
            print('no')
        else:
            print('yes')

    elif command.startswith('de'):
        tree_root.delete(int(content))
    # print tree walk
    else:
        in_order(tree_root)
        print('')
        pre_order(tree_root)
        print('')

    return None


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    array_length = int(_input[0])
    command_list = list(map(lambda x: x.split(), _input[1:]))
    # assert len(command_list) == array_length

    flag, tree_root = False, None
    for each in command_list:
        command, content = each[0], each[-1]
        if (not flag) and command.startswith('in'):
            tree_root = Node(data=int(content))
            flag = True
            continue
        action(command, content)