import sys
import collections

readline = sys.stdin.readline

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1]*n
        self.rank = [0]*n
        self.size = [1]*n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.rank[x] < self.rank[y]:
            self.size[y] += self.size[x]
            self.parents[x] = y
        else:
            self.size[x] += self.size[y]
            self.parents[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def msize(self, x):
        return -self.size[self.find(x)]

def main():
    N, M = map(int, readline().split())
    nodelist = []
    for _ in range(M):
        A, B = map(int, readline().split())
        A -= 1; B -= 1
        nodelist.append((A, B))
    
    uf = UnionFind(N)
    anstmp = (N*(N-1))//2
    anslist = [anstmp]
    for _ in range(M):
        node = nodelist.pop()
        n0 = uf.find(node[0])
        n1 = uf.find(node[1])
        if n0 != n1:
            n0size = uf.size[n0]
            n1size = uf.size[n1]
        else:
            n0size = 0; n1size = 0
        uf.union(node[0], node[1])
        anstmp = anslist[-1]
        ans = anstmp - n0size*n1size
        anslist.append(ans)
    anslist = anslist[:-1]
    for _ in range(len(anslist)):
        ans = anslist.pop()
        print(ans)

if __name__ == "__main__":
    main()
