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
N,M,K = map(int,input().split())
u = UnionFind(N)
friend = [[] for _ in range(N)]
for i in range(M):
    A,B = map(int,input().split())
    friend[A-1].append(B-1)
    friend[B-1].append(A-1)
    u.union(A-1,B-1)
block = [[] for _ in range(N)]
for i in range(K):
    C,D = map(int,input().split())
    block[C-1].append(D-1)
    block[D-1].append(C-1)
ans = [0]*N
for i in range(N):
    ans[i] = u.size(i)-1
    for f in friend[i]:
        if u.find(i)==u.find(f):
            ans[i] -= 1
    for b in block[i]:
        if u.find(i)==u.find(b):
            ans[i] -= 1
print(*ans)