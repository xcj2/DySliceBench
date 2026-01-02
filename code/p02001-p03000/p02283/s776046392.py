class Node:
    def __init__(self, k):
        self.parent = None
        self.childs = [None, None]
        self.key = k


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, z):
        y = None
        x = self.root
        while x != None:
            y = x
            if z.key < x.key:
                x = x.childs[0]
            else:
                x = x.childs[1]
        z.p = y
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.childs[0] = z
        else:
            y.childs[1] = z


def preorder(p):
    s = ""
    if p == None:
        return ""
    s += f"{p.key} "
    s += preorder(p.childs[0])
    s += preorder(p.childs[1])
    return s


def inorder(p):
    s = ""
    if p == None:
        return ""
    s += inorder(p.childs[0])
    s += f"{p.key} "
    s += inorder(p.childs[1])
    return s


n = int(input())

t = Tree()
for i in range(n):
    v = input().split()
    if v[0] == "insert":
        t.insert(Node(int(v[1])))
    else:
        print(" "+inorder(t.root).strip())
        print(" "+preorder(t.root).strip())

