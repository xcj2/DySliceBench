N = int(input())
S = input()
Q = int(input())
qs = [input().split() for i in range(Q)]

def ctoi(c):
    return ord(c) - ord('a')

class BinaryIndexedTree:
    def __init__(self,size):
        self.N = size
        self.bit = [0]*(size+1)
    def add(self,x,w): # 0-indexed
        x += 1
        while x <= self.N:
            self.bit[x] += w
            x += (x & -x)
    def _sum(self,x): # 1-indexed
        ret = 0
        while x > 0:
            ret += self.bit[x]
            x -= (x & -x)
        return ret
    def sum(self,l,r): # [l,r)
        return self._sum(r) - self._sum(l)
    def __str__(self): # for debug
        arr = [self.sum(i,i+1) for i in range(self.N)]
        return str(arr)
bits = [BinaryIndexedTree(N) for i in range(26)]

s = []
for i,c in enumerate(S):
    bits[ctoi(c)].add(i,1)
    s.append(c)

ans = []
for a,b,c in qs:
    if a=='1':
        i = int(b)-1
        bits[ctoi(s[i])].add(i,-1)
        bits[ctoi(c)].add(i,1)
        s[i] = c
    else:
        l,r = int(b)-1,int(c)
        a = 0
        for i in range(26):
            if bits[i].sum(l,r):
                a += 1
        ans.append(a)
print(*ans,sep='\n')