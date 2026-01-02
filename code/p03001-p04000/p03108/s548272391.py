N, M = map(int, input().split())
ab = [tuple(map(lambda x:int(x)-1, input().split())) for _ in range(M)]
 
 
class UnionFind:
    def __init__(self,size):
        self.rank = [-1 for _ in range(size)]
        self.number = [1 for _ in range(size)]
 
    def find(self,x):
        while self.rank[x] >= 0:
            x = self.rank[x]
        return x
 
    def union(self,x,y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 == s2:
            return
        if self.rank[s1] == self.rank[s2]:
            self.rank[s1] -= 1
            self.rank[s2] = s1
            self.number[s1] += self.number[s2]
        elif self.rank[s1] < self.rank[s2]:
            self.rank[s2] = s1
            self.number[s1] += self.number[s2]
        else:
            self.rank[s1] = s2
            self.number[s2] += self.number[s1]
 
 
def main():
    uf = UnionFind(N)
    p = N * (N - 1) // 2
    ans = [p]
    for x, y in reversed(ab):
        px = uf.find(x)
        py = uf.find(y)
        if px != py:
            p -= uf.number[px] * uf.number[py]
            uf.union(px, py)
        ans.append(p)
 
    for a in reversed(ans[:-1]):
        print(a)
 
 
main()
