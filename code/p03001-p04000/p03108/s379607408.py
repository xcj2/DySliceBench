from sys import setrecursionlimit
setrecursionlimit(10**5)

n, m = list(map(int, input().split()))
ab = [list(map(int, input().split())) for _ in range(m)]

class UnionFind(list) :
    def __init__(self, n) :
        super().__init__(range(n))
        self.dic = {i:1 for i in range(n)}
        self.fubensa = n*(n-1)//2

    def find(self, i) :
        if self[i] == i : return i
        self[i] = self.find(self[i])
        return self[i]

    def union(self, x, y) :
        x = self.find(x)
        y = self.find(y)
        self[y] = x
        if x != y :
            self.fubensa -= self.dic[x]*self.dic[y]
            self.dic[x] += self.dic[y]
            del self.dic[y]

    def sameroot(self, x, y) :
        return self.find(x) == self.find(y)

uf = UnionFind(n)
ans = []
for a, b in reversed(ab) :
    ans.append(uf.fubensa)
    uf.union(a-1, b-1)
    
for a in reversed(ans) :
    print(a)