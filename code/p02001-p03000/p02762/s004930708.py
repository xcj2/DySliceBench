import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.length = [1 for _ in range(n)] 

    def makeSet(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.length = [1 for _ in range(n)]

    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.parents[x] = y
            self.length[y] += self.length[x]
        else:
            self.parents[y] = x
            self.length[x] += self.length[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def getLength(self, x):
        x = self.find(x)
        return self.length[x]        

    def isSameGroup(self, x, y):
        return self.find(x) == self.find(y)
 
def main():
    N, M, K = map(int, readline().split())
    friend = [set() for _ in range(N)]
    block = [set() for _ in range(N)]
    uf = UnionFind(N)
    for _ in range(M):
        a, b = map(int, readline().split())
        a-=1
        b-=1
        friend[a].add(b)
        friend[b].add(a)
        uf.unite(a, b)

    for _ in range(K):
        c, d = map(int, readline().split())
        c-=1
        d-=1
        block[c].add(d)
        block[d].add(c)

    for i in range(N):
        cnt = 0
        for blk in block[i]:
            if uf.isSameGroup(i, blk):
                cnt += 1    
        ans = uf.getLength(i)-cnt-len(friend[i])-1
        if i == N-1:
            print(ans)
        else:
            print(ans, end=" ")
if __name__ == '__main__': 
    main()