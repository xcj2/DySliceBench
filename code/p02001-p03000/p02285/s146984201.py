#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
input:
18
insert 8
insert 2
insert 3
insert 7
insert 22
insert 1
find 1
find 2
find 3
find 4
find 5
find 6
find 7
find 8
print
delete 3
delete 7
print

output: finded + in_order + pre_order
yes
yes
yes
no
no
no
yes
yes
 1 2 3 7 8 22
 8 2 1 3 7 22
 1 2 8 22
 8 2 1 22

"""

import sys
import copy


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
                # copy current node as parent
                parent = node

                # recursively find deepest successor(leaf)
                successor = node.right
                while successor.left:
                    parent = successor
                    successor = successor.left

                # replace node with node.next(in-order & leaf)
                node.data = successor.data

                # the real successor has only right child
                if parent.left is successor:
                    parent.left = successor.right

                # the real successor has no left child
                else:
                    parent.right = successor.right
                del successor


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