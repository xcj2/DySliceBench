#python3

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

    n, m, k = map(int, input().split())
    uf = UnionFind(n)

    to = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(lambda x: int(x)-1, input().split())
        to[a].append(b)
        to[b].append(a)
        uf.unite(a, b)

    block = [[] for _ in range(n)]
    block_count = [0 for _ in range(n)]
    for _ in range(k):
        c, d = map(lambda x: int(x)-1, input().split())
        block[c].append(d)
        block[d].append(c)
        if uf.isSameGroup(c, d):
            block_count[c] += 1 
            block_count[d] += 1
   #同じグループ内にいるときのみブロックを引く 
    for i in range(n):
        ans = uf.getLength(i) - len(to[i]) - block_count[i] - 1
        print(ans, end=' ')
main()