from collections import deque, namedtuple

class BinaryTree:
    def __init__(self, t):
        self.t = t

    def setDepth(self, u, d):
        if u == -1:
            return
        self.t[u] = self.t[u]._replace(d = d)
        self.setDepth(self.t[u].l, d + 1)
        self.setDepth(self.t[u].r, d + 1)

    def setHeight(self, u):
        h1 = 0
        h2 = 0
        if self.t[u].l != -1:
            h1 = self.setHeight(self.t[u].l) + 1
        if self.t[u].r != -1:
            h2 = self.setHeight(self.t[u].r) + 1
        self.t[u] = self.t[u]._replace(h = max(h1, h2))
        return self.t[u].h

    def getSibling(self, u):
        if self.t[u].p == -1:
            return -1
        if self.t[self.t[u].p].l not in (u, -1):
            return self.t[self.t[u].p].l
        if self.t[self.t[u].p].r not in (u, -1):
            return self.t[self.t[u].p].r
        return -1

    def printNode(self, i):
        p_ = self.t[i].p
        s_ = self.getSibling(i)
        deg_ = 0
        if self.t[i].l != -1:
            deg_ += 1
        if self.t[i].r != -1:
            deg_ += 1
        dep_ = self.t[i].d
        h_ = self.t[i].h
        if p_ == -1:
            t_ = "root"
        elif deg_ == 0:
            t_ = "leaf"
        else:
            t_ = "internal node"
        print("node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}".format(i, p_, s_,  deg_, dep_, h_, t_))

if __name__ == '__main__':
    n = int(input().rstrip())
    Node = namedtuple('Node', ['p', 'l', 'r', 'd', 'h'])
    t = [Node(-1, -1, -1, -1, -1)] * n
    r = -1
    for i in range(n):
        v, l, r = [int(i) for i in input().rstrip().split(" ")]
        t[v] = t[v]._replace(l = l, r = r)
        if l != -1:
            t[l] = t[l]._replace(p = v)
        if r != -1:
            t[r] = t[r]._replace(p = v)
    for i in range(n):
        if (t[i].p == -1):
            r = i
    x = BinaryTree(t)
    x.setDepth(r, 0)
    x.setHeight(r)
    for i in range(n):
        x.printNode(i)