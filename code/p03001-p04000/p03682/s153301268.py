from operator import itemgetter
import heapq
N = int(input())
X = []
Y = []
for i in range(N):
    x, y = map(int, input().split())
    X.append((x, i))
    Y.append((y, i))
X.sort(key=itemgetter(0))
Y.sort(key=itemgetter(0))

import sys
sys.setrecursionlimit(10**6)


class UnionFind(object):

    def __init__(self, size):
        self.table = [-1 for _ in range(size)]

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
        else:
            return False
u = UnionFind(N)
q = []
for i in range(N-1):
    q.append((X[i+1][0]-X[i][0], X[i+1][1], X[i][1]))
    q.append((Y[i+1][0]-Y[i][0], Y[i+1][1], Y[i][1]))
q.sort(key=itemgetter(0))
ans = 0
for elem in q:
    cost, a, b = elem
    if u.union(a, b):
        ans += cost
print(ans)
