#!python3

def LI():
    return list(map(int, input().split()))

# input
N, M = LI()
XYZ = [LI() for _ in range(M)]


class Node:

    def __init__(self, num):
        self.num = num
        self.parent = None

    def root(self):
        if self.parent is None:
            return self
        self.parent = self.parent.root()
        return self.parent


class UnionFind:

    def __init__(self, n):
        self.n = n
        self.nodes = [Node(i) for i in range(n)]
        self.groups = {i: 1 for i in range(n)}
    
    def union(self, x, y):
        x = self.nodes[x].root().num
        y = self.nodes[y].root().num
        if x == y:
            return
        if self.groups[x] < self.groups[y]:
            x, y = y, x
        self.groups[x] += self.groups[y]
        del self.groups[y]
        self.nodes[y].parent = self.nodes[x]
    
    def same(self, x, y):
        a = self.nodes[x].root()
        b = self.nodes[y].root()
        return True if a == b else False
    

def main():
    uf = UnionFind(N)
    for x, y, z in XYZ:
        uf.union(x - 1, y - 1)
    
    ans = len(uf.groups)
    print(ans)


if __name__ == "__main__":
    main()
