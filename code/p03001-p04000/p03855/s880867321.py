from collections import defaultdict
class UnionFind:
    def __init__(self, num):
        self.table = [-1 for _ in range(num)]

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
            if self.table[s1] <= self.table[s2]:
                self.table[s1] += self.table[s2]
                self.table[s2] = s1
            else:
                self.table[s2] += self.table[s1]
                self.table[s1] = s2
            return True
        return False

N,K,L = map(int,input().split())
u1 = UnionFind(N)
u2 = UnionFind(N)
for _ in range(K):
    p,q = map(int,input().split())
    u1.union(p-1,q-1)
for _ in range(L):
    r,s = map(int,input().split())
    u2.union(r-1,s-1)

d = defaultdict(lambda:0)
for i in range(N):
    d[(u1.find(i),u2.find(i))] += 1

ans = []
for i in range(N):
    ans.append(str(d[(u1.find(i),u2.find(i))]))

ans = ' '.join(ans)
print(ans)