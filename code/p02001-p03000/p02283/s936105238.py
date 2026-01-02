# -*- coding:utf-8 -*-
import sys


class Node(object):
    __slots__ = ["value", "left", "right"]

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinTree(object):
    def __init__(self):
        self._tree = None

    def insert(self, value):
        parent = None
        current = self._tree

        while current is not None:
            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right

        if parent is None:
            self._tree = Node(value)
        elif value < parent.value:
            parent.left = Node(value)
        else:
            parent.right = Node(value)

    def preoder_walk(self):
        def preoder(node):
            result = []
            if node is None:
                pass
            else:
                result.append(node.value)
                result.extend(preoder(node.left))
                result.extend(preoder(node.right))
            return result

        return preoder(self._tree)

    def inorder_walk(self):
        def inorder(node):
            result = []
            if node is None:
                pass
            else:
                result.extend(inorder(node.left))
                result.append(node.value)
                result.extend(inorder(node.right))
            return result

        return inorder(self._tree)


def print_tree(tree):
    print(" " + " ".join([str(val) for val in tree.inorder_walk()]))
    print(" " + " ".join([str(val) for val in tree.preoder_walk()]))


def insert_main(commands):
    tree = BinTree()
    for com in commands:
        if com[0] == "insert":
            tree.insert(int(com[1]))
        elif com[0] == "print":
            print_tree(tree)
        else:
            raise ValueError


if __name__ == "__main__":
    n = int(input())
    commands = [com.split() for com in sys.stdin.readlines()]
    insert_main(commands)