#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
input:
9
insert 30
insert 88
insert 12
insert 1
print
insert 20
insert 17
insert 25
print

output: in_order + pre_order
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
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

        return None

        # def tree_data(self):
        #     """
        #     ???????????°?????????
        #     """
        #     stack = []
        #     node = self
        #     while stack or node:
        #         if node:
        #             print(node.data, 'append')
        #             stack.append(node)
        #             node = node.left
        #             if node:
        #                 print(node.data, 'left')
        #         else:
        #             node = stack.pop()
        #             print(node.data, 'pop')
        #             yield node.data
        #             node = node.right
        #             if node:
        #                 print(node.data, 'right')


def inorder(node):
    """
    ????????????????????????????????¨?????°

    :param node: ??????????????????Node ????±?
    :return:
    """

    if node.left:
        yield from inorder(node.left)
    yield node.data
    if node.right:
        yield from inorder(node.right)


def preorder(node):
    """
    ????????????????????????????????¨?????°

    :param node: ??????????????????Node ????±?
    """

    yield node.data

    for n in [node.left, node.right]:
        if n:
            # require python version >= 3.3
            # equals to:
            # for inner_node in preorder(n):
            #     yield inner_node
            yield from preorder(n)


# def pre_order(node):
#     if node is not None:
#         print('', node.data, end='')
#         pre_order(node.left)
#         pre_order(node.right)
#     return None
#
#
# def in_order(node):
#     if node is not None:
#         in_order(node.left)
#         print('', node.data, end='')
#         in_order(node.right)
#     return None


def action(command, content):
    if command[0] == 'i':
        tree_root.insert(data=int(content))

    elif command[0] == 'p':
        print('', *inorder(node=tree_root))
        print('', *preorder(node=tree_root))
        # print('', *tree_root.tree_data())
        # pre_order(tree_root)
        # print('')

    return None


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    array_length = int(_input[0])
    command_list = list(map(lambda x: x.split(), _input[1:]))
    # assert len(command_list) == array_length
    # print(array_length, *command_list)

    flag, tree_root = False, None
    for each in command_list:
        command, content = each[0], each[-1]
        if (not flag) and command.startswith('in'):
            tree_root = Node(data=int(content))
            flag = True
            continue
        action(command=command, content=content)