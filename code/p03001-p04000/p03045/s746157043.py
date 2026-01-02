import sys
sys.setrecursionlimit(100000)

class UnionFind:
    def __init__(self, num):
        self.p = [x for x in range(num)]
    def root(self, x):
        if self.p[x] == x:
            return x
        else:
            self.p[x] = self.root(self.p[x])
            return self.p[x]
    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx != ry:
            self.p[ry] = rx

def main():
    N, M = (int(x) for x in input().split())
    u = UnionFind(N)

    for i in range(M):
        x,y,_ = map(int, input().split())
        u.unite(x-1, y-1)

    rlist = set()
    for i in range(N):
        rlist.add(u.root(i))

    print(len(rlist))

if __name__ == '__main__':
    main()
