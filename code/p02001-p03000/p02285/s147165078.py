class Node:
    def __init__(self, key:int):
        self.key = key
        self.p = None
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, z:Node):
        y = None
        x = self.root
        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

def Preorder(target:Node):
    yield target.key
    if target.left != None:
        yield from Preorder(target.left)
    if target.right != None:
        yield from Preorder(target.right)

def Inorder(target:Node):
    if target.left != None:
        yield from Inorder(target.left)
    yield target.key
    if target.right != None:
        yield from Inorder(target.right)

def find(target:Node,findkey:int):
    return node_of_key(target, findkey) != None

def node_of_key(target:Node,findkey:int):
    if target.key == findkey:
        return target
    elif target.key > findkey:
        if target.left:
            return node_of_key(target.left, findkey)
    else:
        if target.right:
            return node_of_key(target.right, findkey)
    return None

def min_value_node_of_tree(root:Node):
    if root.left == None:
        return root
    else:
        return min_value_node_of_tree(root.left)

def delete(target:Node):
    if target.left == None and target.right == None:
        if target.key < target.p.key:
            target.p.left = None
        else:
            target.p.right = None
    elif (target.left == None) ^ (target.right == None):
        child = target.left if target.left else target.right
        child.p = target.p
        if target.key < target.p.key:
            target.p.left = child
        else:
            target.p.right = child
    else:
        next_node = min_value_node_of_tree(target.right)
        target.key = next_node.key
        delete(next_node)

from sys import stdin
tree = Tree()
n = int(input())
lines = stdin.readlines()
for line in lines:
    proc,*key = line.split()
    if proc == "insert":
        tree.insert(Node(int(key[0])))
    elif proc == "find":
        print("yes" if find(tree.root, int(key[0])) else "no")
    elif proc == "delete":
        delete(node_of_key(tree.root, int(key[0])))
    else:
        print(" ",end="")
        print(*Inorder(tree.root))
        print(" ",end="")
        print(*Preorder(tree.root))
