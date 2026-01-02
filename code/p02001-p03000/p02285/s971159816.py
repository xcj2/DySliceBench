#coding:utf-8
#1_8_C
class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
class Tree:
    def __init__(self):
        self.root = None

    def insert(self, node):
        y = None # set parent
        x = self.root
        while x is not None:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
    
        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
            node.parent = y
        else:
            y.right = node
            node.parent = y

    def find(self, node, key):
        if node is None:
            return None

        if key == node.key:
            return node
        elif key < node.key:
            return self.find(node.left, key)
        else:
            return self.find(node.right, key)

    def delete(self, key):
        del_node = self.find(self.root, key)
        if del_node.right and del_node.left:
            # del_node has two children
            right_min = del_node.right
            while right_min.left:
                right_min = right_min.left
            tmp = right_min.key
            self.delete(right_min.key)
            del_node.key = tmp
        elif del_node.right or del_node.left:
            # del_node has only one children
            child = del_node.right if del_node.right else del_node.left
            if del_node.parent.right == del_node:
                del_node.parent.right = child
                child.parent = del_node.parent
            else:
                del_node.parent.left = child
                child.parent = del_node.parent
        else:
            # del_node has no child
            if del_node.parent.right == del_node:
                del_node.parent.right = None
            else:
                del_node.parent.left = None


def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(" {}".format(node.key), end = "")
    inorder(node.right)

def preorder(node):
    if node is None:
        return
    print(" {}".format(node.key), end = "")
    preorder(node.left)
    preorder(node.right)

def execute(tree, cmd):
    if cmd[0] == 'insert':
        t.insert(Node(int(cmd[1])))
    elif cmd[0] == 'find':
        if tree.find(tree.root, int(cmd[1])):
            print('yes')
        else:
            print('no')
    elif cmd[0] == 'delete':
        tree.delete(int(cmd[1]))
    else:
        inorder(t.root)
        print()
        preorder(t.root)
        print()

m = int(input())
t = Tree()
for i in range(m):
    execute(t, input().split())