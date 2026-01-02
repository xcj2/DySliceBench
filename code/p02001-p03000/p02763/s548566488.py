import sys
input = sys.stdin.readline
N = int(input())
S = input().rstrip()
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
bits = [BinaryIndexedTree(N) for _ in range(26)]

for i,c in enumerate(S):
    bits[ctoi(c)].add(i,1)

s = list(S)
ans = []
for a,b,c in qs:
    if a=='1':
        x = int(b)-1
        bits[ctoi(c)].add(x,1)
        bits[ctoi(s[x])].add(x,-1)
        s[x] = c
    else:
        b,c = int(b)-1,int(c)
        tmp = 0
        for i in range(26):
            if bits[i].sum(b,c) > 0:
                tmp += 1
        ans.append(tmp)
print(*ans, sep='\n')