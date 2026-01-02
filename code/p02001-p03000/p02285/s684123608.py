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

    def find(self, value):
        current = self._tree

        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right

        return False

    def delete(self, value):
        parent = None
        current = self._tree

        while current.value != value:
            parent = current
            if current is None:
                return
            elif value < current.value:
                current = current.left
            else:
                current = current.right

        if current.left is None and current.right is None:
            if parent.left is current:
                parent.left = None
            else:
                parent.right = None
        elif current.left is None:
            if parent.left is current:
                parent.left = current.right
            else:
                parent.right = current.right
        elif current.right is None:
            if parent.left is current:
                parent.left = current.left
            else:
                parent.right = current.left
        else:
            next_node_parent = current
            next_node = current.right
            while next_node.left is not None:
                next_node_parent = next_node
                next_node = next_node.left

            if next_node.right is None:
                if next_node_parent.left is next_node:
                    next_node_parent.left = None
                else:
                    next_node_parent.right = None
            else:
                if next_node_parent.left is next_node:
                    next_node_parent.left = next_node.right
                else:
                    next_node_parent.right = next_node.right

            current.value = next_node.value

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


def print_yes_no(boolean):
    if boolean:
        print("yes")
    else:
        print("no")


def main(commands):
    tree = BinTree()
    for com in commands:
        if com[0] == "insert":
            tree.insert(int(com[1]))
        elif com[0] == "print":
            print_tree(tree)
        elif com[0] == "find":
            print_yes_no(tree.find(int(com[1])))
        elif com[0] == "delete":
            tree.delete(int(com[1]))
        else:
            raise ValueError


if __name__ == "__main__":
    n = int(input())
    commands = [com.split() for com in sys.stdin.readlines()]
    main(commands)