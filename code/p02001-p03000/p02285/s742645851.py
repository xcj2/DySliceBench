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
        z.parent = y
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.childs[0] = z
        else:
            y.childs[1] = z

    def find(self, k):
        x = self.root
        while x != None:
            if k == x.key:
                return x
            if k < x.key:
                x = x.childs[0]
            else:
                x = x.childs[1]
        return None

    def delete(self, k):
        z = self.find(k)
        if z == None:
            return
        if z.childs[0] == None and z.childs[1] == None:
            p = z.parent
            if p != None:
                for i, v in enumerate(p.childs):
                    if v == z:
                        p.childs[i] = None
                        break
        elif z.childs[0] != None and z.childs[1] != None:
            y = z.childs[1]
            while y.childs[0] != None:
                y = y.childs[0]
            nk = y.key
            self.delete(nk)
            z.key = nk
        else:
            p = z.parent
            c = z.childs[0] if z.childs[0] != None else z.childs[1]
            c.parent = p
            if p != None:
                for i, v in enumerate(p.childs):
                    if v == z:
                        p.childs[i] = c
                        break


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
    elif v[0] == "find":
        print("yes" if t.find(int(v[1])) != None else "no")
    elif v[0] == "delete":
        t.delete(int(v[1]))
    else:
        print(" "+inorder(t.root).strip())
        print(" "+preorder(t.root).strip())

