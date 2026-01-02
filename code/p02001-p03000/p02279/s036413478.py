from collections import deque, namedtuple

class RootedTree:
    def __init__(self, t, n):
        self.t = t
        self.n = n
        self.d = [-1] * n

    def setDepth(self, u, p):
        self.t[u] = self.t[u]._replace(d = p)
        for i in self.getChildren(u):
            self.setDepth(i, p + 1)

    def getChildren(self, u):
        ret = []
        c = self.t[u].l
        while c != -1:
            ret.append(c)
            c = self.t[c].r
        return(ret)

    def printNode(self, i):
        p_ = self.t[i].p
        d_ = self.t[i].d
        c_ = self.getChildren(i)
        if p_ == -1:
            t_ = "root"
        elif len(c_) == 0:
            t_ = "leaf"
        else:
            t_ = "internal node"
        print("node {}: parent = {}, depth = {}, {}, {}".format(i, p_, d_, t_, c_))

if __name__ == '__main__':
    n = int(input().rstrip())
    Node = namedtuple('Node', ['p', 'l', 'r', 'd'])
    t = [Node(-1, -1, -1, -1)] * n
    r = -1
    for i in range(n):
        tmp = deque([int(i) for i in input().rstrip().split(" ")])
        v = tmp.popleft()
        d = tmp.popleft()
        for j in range(d):
            c = tmp.popleft()
            if j == 0:
                t[v] = t[v]._replace(l = c)
            else:
                t[l] = t[l]._replace(r = c)
            l = c
            t[c] = t[c]._replace(p = v)
    for i in range(n):
        if (t[i].p == -1):
            r = i
    x = RootedTree(t, n)
    x.setDepth(r, 0)
    for i in range(n):
        x.printNode(i)
    