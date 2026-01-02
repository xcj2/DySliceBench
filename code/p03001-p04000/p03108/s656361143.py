from collections import defaultdict
class UnionFind:
    def __init__(self, num):
        self.table = [-1 for _ in range(num)]
        self.sz = defaultdict(lambda:1)

    def find(self, x):
        if self.table[x] < 0:
            return x
        else:
            self.table[x] = self.find(self.table[x])
            return self.table[x]

    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)

        if s1 != s2:
            size = self.sz[s1]+self.sz[s2]
            if self.table[s1] <= self.table[s2]:
                self.table[s1] += self.table[s2]
                self.table[s2] = s1
            else:
                self.table[s2] += self.table[s1]
                self.table[s1] = s2
            s = self.find(x)
            self.sz[s] = size
            return True
        return False

    def size(self, x):
        s = self.find(x)
        return self.sz[s]

N,M = map(int,input().split())
u = UnionFind(N)
AB = [list(map(lambda x:int(x)-1,input().split())) for _ in range(M)]
AB = AB[::-1]
ans = [N*(N-1)//2]*M
for i in range(M-1):
    A,B = AB[i]
    ans[i+1] = ans[i]
    if u.find(A) != u.find(B):
        ans[i+1] -= u.size(A)*u.size(B)
        u.union(A,B)
ans = ans[::-1]
for i in range(M):
    print(ans[i])