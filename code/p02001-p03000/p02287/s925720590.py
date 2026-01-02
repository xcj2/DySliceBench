# -*- coding: utf-8 -*-
class BinaryHeap:
    def __init__(self, ary):
        self.nodes = []
        for i, key in enumerate(ary):
            id = i + 1
            parent = id // 2
            if parent:
                parent_key = ary[parent - 1]
            else:
                parent_key = None
            left = 2 * id
            right = 2 * id + 1
            if left <= len(ary):
                left_key = ary[left - 1]
            else:
                left_key = None
            if right <= len(ary):
                right_key = ary[right - 1]
            else:
                right_key = None
            self.nodes.append(Node(id, key, parent_key, left_key, right_key))

    def print(self):
        for node in self.nodes:
            print('node {}: key = {}, '.format(node.id, node.key), end='')
            if type(node.parent_key) == int:
                print('parent key = {}, '.format(node.parent_key), end='')
            if type(node.left_key) == int:
                print('left key = {}, '.format(node.left_key), end='')
            if type(node.right_key) == int:
                print('right key = {}, '.format(node.right_key), end='')
            print()


class Node:
    def __init__(self, id, key, parent_key, left_key, right_key):
        self.id = id
        self.key = key
        self.parent_key = parent_key
        self.left_key = left_key
        self.right_key = right_key


if __name__ == '__main__':
    H = int(input())
    ary = [int(_) for _ in input().split()]
    bh = BinaryHeap(ary)
    bh.print()

