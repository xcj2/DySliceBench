import sys, os
from io import StringIO

class BinaryTree:

    class Node:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None
            self.parent = None


    def __init__(self):
        self.root = None
        self.output = StringIO()

    def insert(self, key):
        if self.root is None:
            self.root = self.Node(key)
        else:
            root = self.root
            temp = None
            while True:
                temp = root
                if key > root.key:
                    root = root.right
                    if root is None:
                        temp.right = self.Node(key)
                        n = temp.right
                        n.parent = temp
                        break
                else:
                    root = root.left
                    if root is None:
                        temp.left = self.Node(key)
                        n = temp.left
                        n.parent = temp
                        break

    def ini_print_inorder(self):
        self.output = StringIO()
        self.print_inorder(self.root)
        return self.output.getvalue()

    def ini_print_preorder(self):
        self.output = StringIO()
        self.print_preorder(self.root)
        return self.output.getvalue()

    def print_inorder(self, node):
        if node is not None:
            self.print_inorder(node.left)
            print(node.key, end = " ", file = self.output)
            self.print_inorder(node.right)

    def print_preorder(self, node):
        if node is not None:
            print(node.key, end = " ", file = self.output)
            self.print_preorder(node.left)
            self.print_preorder(node.right)

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
        root = self.root
        temp = root
        act = ""
        while root is not None:
            if key == root.key:
                # print(root.key, root.left, root.right, root.parent)
                rest = None
                new_leaf = None
                if root.left is None:
                    new_leaf = root.right
                elif root.right is None:
                    new_leaf = root.left
                else:
                    new_leaf, new_leaf_parent = self.get_successor(root.right)
                    rest = 1
                    rest_left = root.left
                    rest_right = root.right
                    if new_leaf == rest_right:
                        rest_right = None
                    # print(rest_left.key, new_leaf.key, new_leaf_parent.key)
                if act != "":
                    setattr(temp, act, new_leaf)
                    # print(new_leaf)
                    if new_leaf is not None:
                        new_node = getattr(temp, act)
                        setattr(new_node, "parent", temp)
                        # print(act, temp.key, key, new_leaf.key, new_node.parent.key)
                else:
                    self.root = new_leaf
                if rest is not None:
                    temp = getattr(temp, act)
                    if rest_right is not None:
                        setattr(temp, "right", rest_right)
                        setattr(rest_right, "parent", temp)
                    setattr(temp, "left", rest_left)
                    setattr(rest_left, "parent", temp)
                    setattr(new_leaf_parent, "left", None)
                    # print("00", temp.key, new_leaf.key, new_leaf.parent.key, new_leaf_parent.key)
                return
            else:
                temp = root
                if key < root.key:
                    root = root.left
                    act = "left"
                else:
                    root = root.right
                    act = "right"

b = BinaryTree()
length = int(input())
for comm in sys.stdin:
    if comm[0] == "i":
        com, num = comm.split(" ")
        b.insert(int(num))
    elif comm[0] == "p":
        print(" ", end = "")
        print((b.ini_print_inorder())[:-1])
        print(" ", end = "")
        print(b.ini_print_preorder()[:-1])
    elif comm[0] == "f":
        com, num = comm.split(" ")
        b.ini_find(int(num))
    else:
        com, num = comm.split(" ")
        b.delete(int(num))
