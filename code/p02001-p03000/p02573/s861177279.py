from collections import deque, defaultdict
import sys
sys.setrecursionlimit(1000000)

class Node:
    def __init__(self, id):
        self.id = id
        self.parent = self.id

N, M = [int(i) for i in input().split()]
P = [Node(i) for i in range(N)]

def root(a):
    if a.id == a.parent:
        return a.id
    else:
        id = root(P[a.parent])
        a.parent = id
        return id

def union(a, b):
    p = root(a)
    q = root(b)
    if p == q:
        return
    else:
        P[q].parent = p

for i in range(M):
    A, B = [int(i)-1 for i in input().split()]
    union(P[A], P[B])

c = defaultdict(int)
for i in range(N):
    c[root(P[i])] += 1
    maxc = 0
for key in c.keys():
    if maxc < c[key]:
        maxc = c[key]
print(maxc)