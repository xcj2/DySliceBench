import sys
readline = sys.stdin.readline

ans = 0
def scomp(S):
    L = 1+max(S)
    table = [0]*L
    for s in S:
        table[s] += 1
    it = [None]*L
    cnt = 0
    for i in range(L):
        it[i] = cnt
        if table[i]:
            cnt += 1
    return it

import sys
readline = sys.stdin.readline

class Node:
    def __init__(self, sigma, depth):
        self.end = False
        self.child = [None] * sigma
        self.depth = depth
        self.count = [0]*sigma
        self.par = None
    def __setitem__(self, i, x):
        self.child[i] = x
    def __getitem__(self, i):
        return self.child[i]

class Trie():
    def __init__(self, sigma):
        self.sigma = sigma
        self.root = Node(sigma, 0)
    
    def add(self, S):
        vn = self.root
        for cs in S:
            if vn[cs] is None:
                vn[cs] = Node(self.sigma, vn.depth + 1)
                vn[cs].par = vn
            vn = vn[cs]
        vn.end = True
    
    def up(self, S):
        vn = self.root
        for cs in S:
            if vn[cs] is None:
                vn[cs] = Node(self.sigma, vn.depth + 1)
            vn = vn[cs]

        k = [0]*self.sigma
        ls = len(S)
        for i in range(ls-1, -1, -1):
            vn = vn.par
            s = S[i]
            k[s] = 1
            for i in range(self.sigma):
                vn.count[i] += k[i]
    
    def count(self, S, ss):
        vn = self.root
        for cs in S:
            if vn[cs] is None:
                vn[cs] = Node(self.sigma, vn.depth + 1)
            vn = vn[cs]
        
        global ans
        ans += vn.count[ss]

ans = 0



N = int(readline())
A = [list(map(lambda x: ord(x)-97, readline().strip()))[::-1] for _ in range(N)]

T = Trie(26)

for a in A:
    T.add(a)
for a in A:
    T.up(a)
for a in A:
    s = a[:-1]
    t = a[-1]
    T.count(s, t)

print(ans-N)