import sys, os
from io import StringIO

class BinaryTree:

    class Node:
        def __init__(self, key, priority = 0):
            self.key = key
            self.left = None
            self.right = None
            self.parent = None
            self.priority = priority

    def __init__(self):
        self.root = None
        self.output = StringIO()


    def insert(self, key, priority):
        self.root = self._insert_main(key, self.root, priority)

    def _insert_main(self, key, node, priority):
        if node is None:
            return self.Node(key, priority)
        else:
            if key > node.key:
                node.right = self._insert_main(key, node.right, priority)
                if node.priority < node.right.priority:
                    node = self.rotate_left(node)
            else:
                node.left = self._insert_main(key, node.left, priority)
                if node.priority < node.left.priority:
                    node = self.rotate_right(node)
            return node


    def rotate_right(self, base):
        left_node = base.left
        # left.right = base
        # base.left = replace
        base.left = left_node.right
        left_node.right = base
        return left_node

    def rotate_left(self, base):
        right_node = base.right
        # replace = right.left
        # right.left = base
        # base.right = replace
        base.right = right_node.left
        right_node.left = base
        return right_node

    def ini_print_inorder(self):
        self.output = StringIO()
        self._print_inorder(self.root)
        return self.output.getvalue()

    def ini_print_preorder(self):
        self.output = StringIO()
        self._print_preorder(self.root)
        return self.output.getvalue()

    def ini_print_postorder(self):
        self.output = StringIO()
        self._print_postorder(self.root)
        return self.output.getvalue()

    def _print_inorder(self, node):
        if node is not None:
            self._print_inorder(node.left)
            print(node.key, end = " ", file = self.output)
            self._print_inorder(node.right)

    def _print_preorder(self, node):
        if node is not None:
            print(node.key, end = " ", file = self.output)
            self._print_preorder(node.left)
            self._print_preorder(node.right)

    def _print_postorder(self, node):
        if node is not None:
            self._print_preorder(node.left)
            self._print_preorder(node.right)
            print(node.key, end = " ", file = self.output)

    def test_insert(self, keys):
        for k in keys:
            self.insert(k)

    def ini_find(self, key):
        print(self.find(key))

    def find(self, key):
        root = self.root
        while root is not None:
            if key == root.key:
                return "yes"
            elif key < root.key:
                root = root.left
            else:
                root = root.right
        return "no"

    def get_successor(self, node):
        parent = node
        while True:
            node = node.left
            if node is None:
                return parent, parent.parent
            parent = node
        return None

    def delete(self, key):
        self.root = self._delete_main(key, self.root)

    def _delete_main(self, key, node):
        if node:
            if key > node.key:
                node.right = self._delete_main(key, node.right)
            elif key < node.key:
                node.left = self._delete_main(key, node.left)
            else:
                if node.right is None and node.left is None:
                    return None
                elif node.right is None:
                    node = self.rotate_right(node)
                elif node.left is None:
                    node = self.rotate_left(node)
                else:
                    if node.left.priority > node.right.priority:
                        node = self.rotate_right(node)
                    else:
                        node = self.rotate_left(node)
                node = self._delete_main(key, node)
        return node

    def _search_min(self, node):
        if node.left is None:
            return node.key
        return self._search_min(node.left)

    def _delete_min(self, node):
        if node.left is None:
            return node.right
        node.left = self._delete_min(node.left)
        return node



b = BinaryTree()
length = int(input())
for _ in range(length):
    comm = input()
    if comm[0] == "i":
        com, num, pri = comm.split(" ")
        b.insert(int(num), int(pri))
    elif comm[0] == "p":
        print(" ", end = "")
        print(b.ini_print_inorder()[:-1])
        print(" ", end = "")
        print(b.ini_print_preorder()[:-1])

    elif comm[0] == "f":
        com, num = comm.split(" ")
        b.ini_find(int(num))
    else:
        com, num = comm.split(" ")
        b.delete(int(num))

