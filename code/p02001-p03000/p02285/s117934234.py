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

output: found + in_order + pre_order
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


class Node(object):
    __slots__ = ('data', 'left', 'right')

    def __init__(self, data):
        self.data = data
        self.left, self.right = None, None

    def insert(self, data):
        """
        Insert data according to BST rules
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
        Find node with given data, tree walk as insert goes
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
        For choosing node deleting strategy
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
            if not children_count:
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
                # current node has two real children(as a partial root)
                # while the real successor couldn't have two real children
                successor = node.right
                while successor.left:
                    successor = successor.left
                copy_data = successor.data
                self.delete(copy_data)
                node.data = copy_data


def in_order_yield(node):
    if node.left:
        yield from in_order_yield(node.left)
    yield node.data
    if node.right:
        yield from in_order_yield(node.right)


def pre_order_yield(node):
    yield node.data

    for child in [node.left, node.right]:
        if child:
            yield from pre_order_yield(child)


def in_order_legacy(node):
    if node.left:
        yield node.left
    yield node.data
    if node.right:
        yield node.right


def pre_order_legacy(node):
    yield node.data
    for child in [node.left, node.right]:
        if child:
            yield from pre_order_yield(child)


def traversal(node, traversal_method):
    stack = [traversal_method(node)]
    while stack:
        last = stack[-1]
        try:
            _new = next(last)
        except StopIteration:
            stack.pop()
        else:
            if isinstance(_new, Node):
                stack.append(traversal_method(_new))
            elif isinstance(_new, int):
                yield _new


def action(_command, _content):
    # start all action from tree_root -- insert, find, delete, print
    if _command.startswith('in'):
        tree_root.insert(int(_content))

    elif _command.startswith('fi'):
        if tree_root.find(int(_content)) == (None, None):
            print('no')
        else:
            print('yes')

    elif _command.startswith('de'):
        tree_root.delete(int(_content))

    # print tree walk
    else:
        # print('', *traversal(tree_root, traversal_method=in_order_legacy))
        # print('', *traversal(tree_root, traversal_method=pre_order_legacy))
        print('', *in_order_yield(tree_root))
        print('', *pre_order_yield(tree_root))

    return None


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    array_length = int(_input[0])
    command_list = list(map(lambda x: x.split(), _input[1:]))
    # assert len(command_list) == array_length

    flag, tree_root = False, None
    allowed_commands = ('insert', 'print', 'delete', 'find')

    for each in command_list:
        command, content = each[0], each[-1]
        # if command not in allowed_commands:
        #     raise SystemExit('Illegal command!')

        # init the whole tree
        if not flag:
            if not command.startswith('in'):
                raise SystemExit('Please insert tree root first.')
            flag, tree_root = True, Node(data=int(content))
            continue
        action(command, content)